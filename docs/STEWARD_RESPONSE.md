# Steward response: per-criterion consensus binding

Date: 2026-08-21

## Request addressed

The steward identified that comparing only `score_bps` and `verdict` allowed
conflicting classifications on equal-weight criteria to preserve the aggregate
result while being stored as inconsistent audit metadata.

## Remediation

The validator now:

1. Requires `criterion_statuses` to be an object containing every immutable
   criterion ID exactly once.
2. Normalizes each status to the allowed enum.
3. Deterministically recomputes `score_bps` and `verdict` from that exact map.
4. Rejects a leader result whose supplied score or verdict is inconsistent with
   its own status map.
5. Independently evaluates the evidence and requires exact equality of the
   complete canonical status map, score, and verdict.

## Regression proof

- `test_validator_rejects_equal_weight_status_swap` gives two criteria equal
  weights, swaps `SATISFIED` and `NOT_SATISFIED`, preserves `5000 / PASS`, and
  confirms validator rejection.
- `test_validator_rejects_status_score_inconsistency` confirms rejection when a
  `SATISFIED` map is paired with `0 / FAIL`.
- Full standalone result: `5 passed`.
- GenVM AST safety lint: 3 checks passed.

## Matching StudioNet deployment

- Contract: `0x0d4e0AF51b27894fd8d81b7fD98400e04564CCC6`
- Deployment transaction: `0x063e7eab79b1a471bfca662ee293e217b882316082a231106984490dee363db4`
- Resolution transaction: `0xe456873aa25ab80f588d5e800c06a20b956d99b41da127c40a76f471e502197f`
- Source SHA-256: `6849513f89e032d99c44609c6eeaf2991f83c9f20413fac12a369446de9ab4a9`
- Deployment and resolution: `FINALIZED`, execution `SUCCESS`.

The live source was unavailable to the selected validators, so resolution
correctly finalized as `INCONCLUSIVE` with both criterion statuses
`INCONCLUSIVE`, score `0`, and verdict `INCONCLUSIVE`. This is the intended
fail-closed path; the receipt still demonstrates majority consensus on one
complete, internally consistent status map.
