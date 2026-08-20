# StudioNet verification

Verification date: 2026-08-20  
Network: StudioNet (chain ID 61999)  
CLI: 0.39.2

## Contract and transactions

- Contract: `0xfF506e1728F302C582360E57fbA0aCbf8769EF28`
- Explorer: https://explorer-studio.genlayer.com/address/0xfF506e1728F302C582360E57fbA0aCbf8769EF28
- Deployment transaction: `0xf05e4d3848bc9608c796b7ac69dcc1330c3a93b0b4e76310a4a1520a89bbda6b`
- Live resolution transaction: `0xc24cccf47da9cfe1613ae811de97a936794f5d2494274dcdba11e1b67e0a5655`

Both transactions are `FINALIZED` and executed successfully. The consensus
result is `MAJORITY_AGREE` with three agree votes; two validators became idle
after quorum was reached.

## Source and schema

- Repository source SHA-256: `1d29ff18e09910b4d04ae4d4659f60f9bef4597c82da514defbf1292696be6f8`
- StudioNet source SHA-256: `1d29ff18e09910b4d04ae4d4659f60f9bef4597c82da514defbf1292696be6f8`
- Exact source match: yes
- StudioNet schema retrieval: succeeded

## Current state

- Status: `RESOLVED`
- Attempts: 1
- Verdict: `PASS`
- Score: 10,000 basis points
- Criterion statuses: `chain-id = SATISFIED`, `production-like = SATISFIED`

The standalone repository suite passed 3 tests on 2026-08-20. GenVM AST safety
lint passed. SDK semantic lint could not run because the current linter artifact
omits the contract's pinned runner tar; this is a toolchain packaging limitation.
