# SKY130 signoff record

This record identifies the reproducible physical implementation that passed
the official Tiny Tapeout TTSKY26c workflow. It does not claim that ordering
silicon has occurred.

## Reproducibility

| Item | Value |
| --- | --- |
| Source commit | `639bf9d58074b700f2d4e8c9460307061e587942` |
| GitHub Actions run | `33257864667` |
| GDS job | `99114612355` (passed) |
| Gate-level test job | `99115460127` (passed) |
| Tiny Tapeout precheck job | `99115460212` (passed) |
| Flow | LibreLane 3.0.5 |
| PDK | `sky130A`, open_pdks `8afc8346a57fe1ab7934ba5a6056ea8b43078e71` |
| Footprint | 1x2 digital tiles |

Workflow URL:
<https://github.com/WaiMingLee888/RISC-V/actions/runs/33257864667>

## Signoff results

| Check | Result |
| --- | --- |
| Extracted hold timing | 0 violations; worst slack +0.0020 ns |
| Extracted setup timing | 0 violations; worst slack +23.1690 ns |
| Detailed-routing DRC | 0 |
| Magic DRC | 0 |
| LVS | Circuits match uniquely; 0 errors or differences |
| Antenna | 0 violating nets and 0 violating pins |
| Power-grid violations | 0 |
| Tiny Tapeout precheck | All listed checks passed |
| Extracted-netlist gate-level simulation | Passed (`test_start`, seed 1788014427) |

The post-global-route repair inserted 82 hold buffers. Final standard-cell
utilization was 79.2096%. The final timing report also records max-slew
warnings at slow corners (378 at the worst corner) and 47 max-fanout warnings.
These were non-fatal in the official flow, whose aggregate design-violation
metric is zero; they are disclosed here rather than represented as absent.

## Artifact integrity

The GitHub artifact archive digests reported by Actions are:

| Artifact | SHA-256 |
| --- | --- |
| `GDS_logs` | `87bcb1094e7ee28f0c2febdcd52d8784222088bcc90c8fca0efb6803f99c0127` |
| `tt_submission` | `82ee0328b3e808809549f551954a6bb3a792dd094039b9499de71457a1737253` |
| `gds_render` | `3565005444344bc597ac68243dae18194ba513d36396e18ff5e96e71e29496bb` |
| `gatelevel_test_results` | `5348b624774371a78895c6340026f39fcd22564515dc524843c1704c690cf1fb` |
| `precheck_reports` | `f47160ef7ebc36c157e4889953006640fec7b408477f845b32bb244e88345954` |

Hashes of principal extracted files are:

| File | SHA-256 |
| --- | --- |
| GDSII | `e11fd629af63004bddea932766bb0332571e67668d906ca0cc2ec22e2bc129f8` |
| OASIS | `304f7f164f7f4da1c1cca458c3080f598c27a4db4eda20c6987836a7f5a1c31f` |
| Gate-level Verilog | `6fe876bb868e570f1ea7c67b5479232e491d0b66a96558eb6985a04b8dc41c30` |
| Nominal SPEF | `72c5abf15a0175a6f4d36ee074af48b35f1ffb6d001394294550e490daf39f85` |
| Final metrics JSON | `d4968282f231b637ee4c0b4c3c290a06e784abcec695d77154eeab5d616e5318` |
| GDS render PNG | `1e5218c8dfd680ce8ae04c36bbfe3c9fba94e0c433e5c9556c4a9aa280592d78` |

## Cost boundary

The project uses two digital tiles. Tiny Tapeout's current SKY130 rate is
EUR 70 per tile, so silicon area is EUR 140. A development kit, taxes, and
shipping are additional. The live calculator is:
<https://app.tinytapeout.com/calculator?pcbs=0&tiles=2>.

