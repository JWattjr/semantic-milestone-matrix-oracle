# GenLayer Portal submission

**Contribution type:** Builder → Intelligent Contracts  
**Title:** Semantic Milestone Matrix Oracle  
**Contribution date:** August 12, 2026

## Notes / Description

Built and deployed an MIT-licensed Semantic Milestone Matrix Oracle, a reusable
GenLayer Intelligent Contract for grants, roadmap predictions, delivery quests,
and milestone escrow gates. It freezes up to 16 weighted qualitative criteria,
a threshold, bounded public evidence, and deadline; the owner may append and
lock evidence only before the cutoff. Leader and validators independently
classify each criterion as SATISFIED, NOT_SATISFIED, or INCONCLUSIVE. A custom
equivalence function independently recomputes and compares the consequential
integer basis-point score and PASS/FAIL/INCONCLUSIVE verdict; per-criterion
statuses remain audit metadata. All-source outages fail closed without invoking
an LLM, private-network evidence is rejected, and terminal writes are
idempotent. Includes pinned GenVM source, consensus tests, security audit, test
matrix, and StudioNet/Bradbury deployment records. It is a decision primitive
and deliberately contains no payout code.

## Evidence to add

1. GitHub Repository — https://github.com/JWattjr/semantic-milestone-matrix-oracle
2. GitHub File — https://github.com/JWattjr/semantic-milestone-matrix-oracle/blob/main/contracts/SemanticMilestoneMatrix.py
3. GitHub File — https://github.com/JWattjr/semantic-milestone-matrix-oracle/blob/main/tests/test_milestone.py
4. GitHub File — https://github.com/JWattjr/semantic-milestone-matrix-oracle/blob/main/docs/SECURITY_AUDIT.md
5. GitHub File — https://github.com/JWattjr/semantic-milestone-matrix-oracle/blob/main/docs/TEST_MATRIX.md
6. GitHub File — https://github.com/JWattjr/semantic-milestone-matrix-oracle/blob/main/deployments/studionet.json
7. GitHub File — https://github.com/JWattjr/semantic-milestone-matrix-oracle/blob/main/deployments/bradbury.json
8. GenLayer Explorer Contract — https://explorer-bradbury.genlayer.com/address/0xB3886D3F95577822f361d6DBB2D706cCc6E70B49
