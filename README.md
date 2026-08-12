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
the consequential score and verdict before on-chain state changes. Per-criterion
statuses remain available for audit.

## Lifecycle and API

- Deploy in `OPEN` with weighted criteria, threshold, evidence, and deadline.
- The owner may call `add_evidence()` and `lock_evidence()` before the deadline.
- Call `resolve()` after the deadline; deterministic integer math derives the
  score and terminal verdict.
- Read the canonical result with `get_state()` and consume it only after
  GenLayer finality.

## Live evidence

- [StudioNet contract](https://explorer-studio.genlayer.com/address/0xfF506e1728F302C582360E57fbA0aCbf8769EF28)
- [Bradbury contract](https://explorer-bradbury.genlayer.com/address/0xB3886D3F95577822f361d6DBB2D706cCc6E70B49)
- Exact receipts and current finality are recorded in `deployments/`.

## Verify

```powershell
python -m pip install -r requirements.txt
genvm-lint check contracts/SemanticMilestoneMatrix.py
pytest tests -v
```

See `docs/SECURITY_AUDIT.md`, `docs/TEST_MATRIX.md`, and
`PORTAL_SUBMISSION.md` for reviewer evidence.
