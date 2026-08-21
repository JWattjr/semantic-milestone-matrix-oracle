import json


def _deploy(direct_deploy):
    return direct_deploy(
        "contracts/SemanticMilestoneMatrix.py",
        "milestone-1",
        [{"id": "docs", "description": "Documentation is public", "weight": 10000}],
        ["https://example.org/docs"],
        "2030-01-01T00:00:00Z",
        7000,
    )


def test_scores_and_validates_consensus(direct_vm, direct_deploy):
    contract = _deploy(direct_deploy)
    direct_vm.warp("2031-01-01T00:00:00Z")
    direct_vm.mock_web(r".*", {"status": 200, "body": "public docs"})
    direct_vm.mock_llm(r".*", json.dumps({"criteria": [{"id": "docs", "status": "SATISFIED"}]}))
    result = contract.resolve()
    assert result["score_bps"] == 10000
    assert result["verdict"] == "PASS"
    assert direct_vm.run_validator()
    assert not direct_vm.run_validator(leader_result={
        "criterion_statuses": {"docs": "NOT_SATISFIED"}, "score_bps": 0, "verdict": "FAIL"
    })


def test_outage_is_inconclusive(direct_vm, direct_deploy):
    contract = _deploy(direct_deploy)
    direct_vm.warp("2031-01-01T00:00:00Z")
    direct_vm.mock_web(r".*", {"status": 503, "body": "offline"})
    assert contract.resolve()["verdict"] == "INCONCLUSIVE"


def test_validator_rejects_equal_weight_status_swap(direct_vm, direct_deploy):
    contract = direct_deploy(
        "contracts/SemanticMilestoneMatrix.py",
        "milestone-swap-regression",
        [
            {"id": "docs", "description": "Documentation is public", "weight": 5000},
            {"id": "release", "description": "Release is production ready", "weight": 5000},
        ],
        ["https://example.org/docs"],
        "2030-01-01T00:00:00Z",
        5000,
    )
    direct_vm.warp("2031-01-01T00:00:00Z")
    direct_vm.mock_web(r".*", {"status": 200, "body": "public docs; release is not production ready"})
    direct_vm.mock_llm(
        r".*",
        json.dumps({"criteria": [
            {"id": "docs", "status": "SATISFIED"},
            {"id": "release", "status": "NOT_SATISFIED"},
        ]}),
    )
    result = contract.resolve()
    assert result["score_bps"] == 5000
    assert result["verdict"] == "PASS"
    assert direct_vm.run_validator()

    # Same score and verdict, conflicting per-criterion classifications.
    assert not direct_vm.run_validator(leader_result={
        "criterion_statuses": {
            "docs": "NOT_SATISFIED",
            "release": "SATISFIED",
        },
        "score_bps": 5000,
        "verdict": "PASS",
    })


def test_validator_rejects_status_score_inconsistency(direct_vm, direct_deploy):
    contract = _deploy(direct_deploy)
    direct_vm.warp("2031-01-01T00:00:00Z")
    direct_vm.mock_web(r".*", {"status": 200, "body": "public docs"})
    direct_vm.mock_llm(r".*", json.dumps({"criteria": [{"id": "docs", "status": "SATISFIED"}]}))
    contract.resolve()

    assert not direct_vm.run_validator(leader_result={
        "criterion_statuses": {"docs": "SATISFIED"},
        "score_bps": 0,
        "verdict": "FAIL",
    })
