# GenLayer Portal submission

**Contribution type:** Builder → Intelligent Contracts  
**Title:** Semantic Milestone Matrix Oracle  
**Contribution date:** Use the actual date of the submitted release.

## Notes / Description

Built and deployed an MIT-licensed Semantic Milestone Matrix Oracle, a reusable
GenLayer Intelligent Contract for grants, roadmap predictions, delivery quests,
and milestone escrow gates. It freezes up to 16 weighted qualitative criteria,
a threshold, bounded public evidence, and deadline; the owner may append and
lock evidence only before the cutoff. Leader and validators independently
classify each criterion as SATISFIED, NOT_SATISFIED, or INCONCLUSIVE. A custom
equivalence function compares the complete criterion map, deterministic integer
basis-point score, and PASS/FAIL/INCONCLUSIVE verdict. All-source outages fail
closed without invoking an LLM, private-network evidence is rejected, and
terminal writes are idempotent. Includes pinned GenVM source, consensus tests,
security audit, test matrix, and StudioNet/Bradbury deployment records. It is a
decision primitive and deliberately contains no payout code.

## Evidence to add

1. GitHub Repository — replace with the private repository URL.
2. GitHub File — `contracts/SemanticMilestoneMatrix.py`.
3. GitHub File — `tests/test_milestone.py`.
4. GitHub File — `docs/SECURITY_AUDIT.md`.
5. GitHub File — `docs/TEST_MATRIX.md`.
6. GitHub File — `deployments/studionet.json`.
7. GitHub File — `deployments/bradbury.json`.
8. GenLayer Explorer Contract — replace with the finalized Bradbury address URL.
