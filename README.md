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
the complete canonical per-criterion status map plus its deterministically
derived score and verdict before on-chain state changes. A status swap cannot be
accepted merely because equal weights preserve the aggregate score.

## Lifecycle and API

- Deploy in `OPEN` with weighted criteria, threshold, evidence, and deadline.
- The owner may call `add_evidence()` and `lock_evidence()` before the deadline.
- Call `resolve()` after the deadline; deterministic integer math derives the
  score and terminal verdict.
- Read the canonical result with `get_state()` and consume it only after
  GenLayer finality.

## Live evidence

- [Corrected StudioNet contract](https://explorer-studio.genlayer.com/address/0x0d4e0AF51b27894fd8d81b7fD98400e04564CCC6)
- The finalized deployment, live resolution, state, source-hash match, and
  receipt identifiers are recorded in `deployments/studionet.json` and
  `docs/STUDIONET_VERIFICATION.md`.

## Verify

```powershell
python -m pip install -r requirements.txt
genvm-lint check contracts/SemanticMilestoneMatrix.py
pytest tests -v
```

See `docs/SECURITY_AUDIT.md`, `docs/TEST_MATRIX.md`, and
`PORTAL_SUBMISSION.md` for reviewer evidence.
