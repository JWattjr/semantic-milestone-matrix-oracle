# Security and consensus audit: SemanticMilestoneMatrix

Audit date: 2026-08-12
Steward-requested remediation: 2026-08-21
Scope: `contracts/SemanticMilestoneMatrix.py`
Method: manual review, GenVM AST lint, SDK schema validation, direct-mode
tests, malicious-leader checks, and hosted-network receipt inspection.

## Result

No unresolved critical or high-severity issue was found after remediation.
The oracle evaluates frozen weighted criteria; it contains no escrow or payout
logic.

## Remediated findings

| ID | Severity | Finding | Remediation |
| --- | --- | --- | --- |
| SM-01 | Medium | An all-evidence outage could reach the LLM. | Return a deterministic `INCONCLUSIVE` verdict and zero score when no source is available. |
| SM-02 | Medium | Evidence URLs allowed private/internal targets. | Require bounded public HTTPS hosts and reject private literals, internal suffixes, userinfo, and non-default ports. |
| SM-03 | Medium | Nondeterministic closures captured storage-backed criteria/evidence. | Snapshot canonical criteria, an ordinary URL list, and threshold before `run_nondet_unsafe`; closures contain no `self`. |
| SM-04 | High | Equal-weight criteria could swap conflicting classifications while preserving the same score and verdict, allowing inconsistent audit metadata to pass equivalence. | Canonicalize the complete `criterion_statuses` map, require every criterion exactly once, recompute score/verdict from that map, reject internal inconsistencies, and require exact map agreement with the validator's independent evaluation. |
| SM-05 | Low | Float-producing score division risked nondeterministic rounding. | Use deterministic integer floor division for basis-point scoring. |
| SM-06 | Low | CLI-decoded JSON, malformed bytes, and loose return wrappers needed hardening. | Canonicalize inputs, safely decode bounded bytes, and require `gl.vm.Return`. |

## Residual risks

- Criteria quality and weights are chosen by the deployer and must be reviewed
  before funds or reputation depend on them.
- Ambiguous prose can yield validator disagreement, which correctly blocks a
  forced pass/fail result.
- Evidence authenticity remains external to the contract.
- DNS rebinding requires reviewed domains or an explicit allowlist.

## Verification evidence

- Pinned GenVM runner; all 3 GenVM AST safety checks pass.
- Standalone direct suite: 5 passed, including outage, malicious-leader,
  equal-weight status-swap, and score/verdict consistency cases.
- Corrected StudioNet deployment finalized with `SUCCESS`, 3 agree / 2 idle.
- Corrected resolution finalized with `SUCCESS`, 3 agree / 1 disagree / 1 idle;
  the unavailable source correctly produced a complete `INCONCLUSIVE` map,
  score 0, and verdict `INCONCLUSIVE`.
- Corrected source SHA-256:
  `6849513f89e032d99c44609c6eeaf2991f83c9f20413fac12a369446de9ab4a9`.
- Re-verification AST lint passed. Deeper SDK validation was unavailable because
  the current linter artifact omits the pinned runner tar; StudioNet source and
  schema retrieval both succeeded.

This is an engineering assessment, not formal verification or a financial or
legal guarantee.
