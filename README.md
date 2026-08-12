# Semantic Milestone Matrix Oracle

A standalone GenLayer Intelligent Contract for grants, roadmap markets,
delivery quests, and milestone escrow gates.

It freezes weighted natural-language criteria, a threshold, evidence URLs, and
a deadline. Before the deadline the owner may append bounded public evidence
and lock the set. Afterward, validators independently classify every criterion
as `SATISFIED`, `NOT_SATISFIED`, or `INCONCLUSIVE`; deterministic integer math
derives a basis-point score and `PASS`, `FAIL`, or `INCONCLUSIVE` verdict.

## GenLayer-native decision

Qualitative deliverables cannot be safely reduced to one API response. The
leader and validators independently evaluate the immutable matrix, then compare
criterion statuses, score, and verdict before on-chain state changes.

## Verify

```powershell
python -m pip install -r requirements.txt
genvm-lint check contracts/SemanticMilestoneMatrix.py
pytest tests -v
```

See `docs/SECURITY_AUDIT.md`, `docs/TEST_MATRIX.md`, and
`PORTAL_SUBMISSION.md` for reviewer evidence.
