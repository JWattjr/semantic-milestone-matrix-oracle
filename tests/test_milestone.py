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
