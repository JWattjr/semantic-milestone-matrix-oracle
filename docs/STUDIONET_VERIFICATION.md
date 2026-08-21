# StudioNet verification

Verification date: 2026-08-21
Network: StudioNet (chain ID 61999)
CLI: 0.39.2

## Corrected contract and transactions

- Contract: `0x0d4e0AF51b27894fd8d81b7fD98400e04564CCC6`
- Explorer: https://explorer-studio.genlayer.com/address/0x0d4e0AF51b27894fd8d81b7fD98400e04564CCC6
- Deployment transaction: `0x063e7eab79b1a471bfca662ee293e217b882316082a231106984490dee363db4`
- Live resolution transaction: `0xe456873aa25ab80f588d5e800c06a20b956d99b41da127c40a76f471e502197f`

Both transactions are `FINALIZED` and executed successfully. Deployment reached
`MAJORITY_AGREE` with three agree votes and two validators cancelled after
quorum. Resolution reached `MAJORITY_AGREE` in two rounds with three agree, one
disagree, and one validator cancelled after quorum.

## Source and schema

- Repository source SHA-256: `6849513f89e032d99c44609c6eeaf2991f83c9f20413fac12a369446de9ab4a9`
- Exact deployment source used by StudioNet: yes
- StudioNet source retrieval: succeeded
- StudioNet schema retrieval: succeeded

## Live consensus result

- Status: `INCONCLUSIVE`
- Attempts: 1
- Verdict: `INCONCLUSIVE`
- Score: 0 basis points
- Canonical criterion statuses: `chain-id = INCONCLUSIVE`, `gasless = INCONCLUSIVE`

The selected validators could not retrieve the public documentation source, so
the contract correctly failed closed. The finalized receipt demonstrates that
the corrected equivalence function processes and stores one complete canonical
status map whose score and verdict are internally consistent. The regression
suite separately proves that an equal-weight status swap with the same score and
verdict is rejected.

The standalone suite passed 5 tests on 2026-08-21. GenVM AST safety lint passed
all 3 checks. SDK semantic lint could not run because the installed linter bundle
omits the contract's pinned runner tar; this is a toolchain packaging limitation.
