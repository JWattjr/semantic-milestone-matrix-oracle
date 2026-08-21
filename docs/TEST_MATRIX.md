# Test matrix

| Requirement | Direct test | Consensus/integration test |
| --- | --- | --- |
| Constructor validation | Invalid JSON, duplicate IDs, bad URL, bad deadline | Deployment rejection on invalid args |
| Access control | Owner-only evidence/review methods | Unauthorized transaction fails |
| Deadline enforcement | Resolve before deadline reverts | Same on a real network timestamp |
| Happy-path decision | Mock web/LLM produces canonical result | Five-validator agreement |
| Malicious leader | Mock leader result differs from independent result | Validator disagreement/rotation |
| Equal-weight status swap | Conflicting criterion maps with identical score/verdict are rejected | Validators must agree on the complete canonical status map |
| Status/result consistency | A status map paired with a false score or verdict is rejected | Stored map, score, and verdict derive from one accepted candidate |
| Missing source | Mock 4xx/5xx or unavailable page | Fail-closed unresolved/unavailable state |
| Prompt injection | Evidence contains fake instructions | Result still follows frozen schema/policy |
| Replay/idempotency | Repeat terminal resolve | Repeat finalized transaction is safe |
| Boundary semantics | K-of-N, threshold, trigger routing, rulebook status | Same result under consensus |
| Nondeterministic storage isolation | AST asserts no `self` reference in leader/validator closures | Live receipt must contain no storage-capture warning |

The direct tests are intentionally small and deterministic. The StudioNet
deployment manifest records the live contract address, deployment transaction,
schema/state verification, source hash, and consensus transaction. A live
`UNRESOLVED` or `INCONCLUSIVE` result is a passing safety
test when the public evidence does not support a terminal judgment.

## Recorded results — 2026-08-12

- Standalone suite: 3 passed.
- Six-contract aggregate suite: 28 passed, 1 environment-only skip.
- GenVM lint and SDK schema validation: passed.
- StudioNet: finalized deployment plus finalized `PASS / 10000 bps` test;
  leader execution `SUCCESS`, 3 agree / 2 idle, no storage-capture warning.

## Re-verification — 2026-08-20

- Standalone suite: 3 passed.
- GenVM AST safety lint: passed.
- StudioNet deployed source hash: exact repository match.
- StudioNet schema and current state reads: succeeded.
- Deployment and live resolution receipts: `FINALIZED` with successful execution.
- SDK semantic lint was blocked by a missing pinned-runner tar in the current
  linter artifact, not by a contract diagnostic.

## Steward remediation — 2026-08-21

- Standalone suite: 5 passed.
- Added an equal-weight swap regression proving that conflicting per-criterion
  classifications cannot pass with the same aggregate score and verdict.
- Added a consistency regression proving that the validator rejects a status
  map paired with a false score or verdict.
- GenVM AST safety lint: 3 checks passed. SDK semantic lint remains blocked by
  the installed linter bundle's missing pinned-runner tar.
