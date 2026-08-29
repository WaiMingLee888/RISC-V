# TTSKY26c submission handoff

The design is technically ready for the Tiny Tapeout submission application.
Payment and commercial submission have **not** been performed.

## Exact candidate

- Repository: <https://github.com/WaiMingLee888/RISC-V>
- Signed-off physical commit: `42259b9dacef690617f9a22234304898dba2b3c4`
- Immutable tag: `nanov-ttsky26c-gds-33266497329`
- Official workflow: <https://github.com/WaiMingLee888/RISC-V/actions/runs/33266497329>
- Project top: `tt_um_WaiMingLee888_nanov`
- Shuttle: `TTSKY26c`
- Area: `1x2`, two digital tiles

Later commits on `main` update documentation only; the audited physical source
and configuration are unchanged. Use the tag above when comparing artifacts.

## Cost and schedule boundary

Tiny Tapeout currently lists TTSKY26c as open with a 2026-09-07 submission
deadline. The public price is EUR 70 per digital tile, making this project's
silicon-space charge EUR 140. Development hardware, taxes, and shipping are
separate. Tile availability can run out before the deadline.

Authoritative current pages:

- <https://tinytapeout.com/chips/>
- <https://app.tinytapeout.com/calculator?pcbs=0&tiles=2>
- <https://app.tinytapeout.com/prepurchase>

## User-authorized commercial steps

These steps require the owner's account and approval because they create an
order or payment obligation:

1. Sign in to <https://app.tinytapeout.com/> using GitHub account
   `WaiMingLee888`.
2. Select the open `TTSKY26c` shuttle and add the repository URL above.
3. Confirm that the imported project reports `1x2` and top module
   `tt_um_WaiMingLee888_nanov`.
4. Pull the repository and require all submission checks to pass.
5. Compare the imported source with the immutable tag and review
   [`SIGNOFF.md`](SIGNOFF.md) and [`K3_REVIEW.md`](K3_REVIEW.md).
6. Reserve/purchase two digital tiles only after confirming the displayed
   price, currency, development-kit option, tax, shipping, and delivery terms.
7. Submit the final revision before the deadline and save the Tiny Tapeout
   project/submission identifier in this document.

## Do not substitute the Linux design

This low-cost NanoV candidate is bare-metal RV32E and cannot run Linux. The
separate KianV RV32IMA Linux-capable SoC requires 8x2 tiles and is a much more
expensive project; it must not be selected accidentally during checkout.
