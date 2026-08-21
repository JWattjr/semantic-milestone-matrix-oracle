# GenLayer Portal submission

**Contribution type:** Builder → Intelligent Contracts  
**Title:** Semantic Milestone Matrix Oracle  
**Contribution date:** August 21, 2026

## Notes / Description

Built and deployed an MIT-licensed Semantic Milestone Matrix Oracle, a reusable
GenLayer Intelligent Contract for grants, roadmap predictions, delivery quests,
and milestone escrow gates. It freezes up to 16 weighted qualitative criteria,
a threshold, bounded public evidence, and deadline; the owner may append and
lock evidence only before the cutoff. Leader and validators independently
classify each criterion as SATISFIED, NOT_SATISFIED, or INCONCLUSIVE. Following
steward review, the validator now canonicalizes and compares the complete
per-criterion status map, recomputes score and verdict from that map, and rejects
missing criteria, equal-weight status swaps, or inconsistent score/verdict pairs.
Outages fail closed, private-network evidence is rejected, and terminal writes
are idempotent. Includes pinned GenVM source, five regression
tests, security audit, test matrix, steward response, and corrected StudioNet
deployment records. It is a decision primitive with no payout code.

## Evidence to add

1. GitHub Repository — https://github.com/JWattjr/semantic-milestone-matrix-oracle
2. GitHub File — https://github.com/JWattjr/semantic-milestone-matrix-oracle/blob/main/contracts/SemanticMilestoneMatrix.py
3. GitHub File — https://github.com/JWattjr/semantic-milestone-matrix-oracle/blob/main/tests/test_milestone.py
4. GitHub File — https://github.com/JWattjr/semantic-milestone-matrix-oracle/blob/main/docs/SECURITY_AUDIT.md
5. GitHub File — https://github.com/JWattjr/semantic-milestone-matrix-oracle/blob/main/docs/TEST_MATRIX.md
6. GitHub File — https://github.com/JWattjr/semantic-milestone-matrix-oracle/blob/main/deployments/studionet.json
7. GitHub File — https://github.com/JWattjr/semantic-milestone-matrix-oracle/blob/main/docs/STEWARD_RESPONSE.md
8. GenLayer Explorer Contract — https://explorer-studio.genlayer.com/address/0x0d4e0AF51b27894fd8d81b7fD98400e04564CCC6
