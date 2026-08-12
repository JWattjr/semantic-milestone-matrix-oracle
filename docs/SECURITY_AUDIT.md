# Security and consensus audit: SemanticMilestoneMatrix

Audit date: 2026-08-12
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
| SM-04 | Medium | Per-criterion diagnostic variation could reject the same consequential decision. | Independently recompute and compare `verdict` and `score_bps`; retain criterion statuses for audit. |
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

- Pinned GenVM runner; GenVM lint and SDK validation pass.
- Standalone direct suite: 3 passed, including outage and malicious-leader
  cases.
- StudioNet deployment and resolution finalized with `SUCCESS`, 3 agree / 2
  idle, and no storage warning.
- Live result: both criteria `SATISFIED`, score 10,000 bps, verdict `PASS`.
- Bradbury status is tracked independently in its deployment manifest.

This is an engineering assessment, not formal verification or a financial or
legal guarantee.
