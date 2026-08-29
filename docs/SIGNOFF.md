# SKY130 signoff record

This record identifies the reproducible physical implementation that passed
the official Tiny Tapeout TTSKY26c workflow. It does not claim that ordering
silicon has occurred.

## Reproducibility

| Item | Value |
| --- | --- |
| Source commit | `42259b9dacef690617f9a22234304898dba2b3c4` |
| GitHub Actions run | `33266497329` |
| GDS job | `99137368659` (passed) |
| Gate-level test job | `99138277306` (passed) |
| Tiny Tapeout precheck job | `99138277268` (passed) |
| Flow | LibreLane 3.0.5 |
| PDK | `sky130A`, open_pdks `8afc8346a57fe1ab7934ba5a6056ea8b43078e71` |
| Footprint | 1x2 digital tiles |

Workflow URL:
<https://github.com/WaiMingLee888/RISC-V/actions/runs/33266497329>

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
| Extracted-netlist gate-level simulation | Passed (`test_start`, seed 1788026096) |

The post-global-route repair inserted 82 hold buffers. Final standard-cell
utilization was 79.2096%. The final timing report also records max-slew
warnings at slow corners (378 at the worst corner) and 47 max-fanout warnings.
These were non-fatal in the official flow, whose aggregate design-violation
metric is zero; they are disclosed here rather than represented as absent.

## Artifact integrity

The GitHub artifact archive digests reported by Actions are:

| Artifact | SHA-256 |
| --- | --- |
| `GDS_logs` | `b10e7359bf3db63fb0e5a76bff1b2ac26da0bbf77dfb68a2b1b70b7cc6cd090f` |
| `tt_submission` | `1642a5f32800f8003cb87326adaa42cd040712eefa4bd1f4d7751f15734c0c79` |
| `gds_render` | `705b2141e3184dc90b84c37be3883853a0cc6e432102bbb6da4c448d0a3a7936` |
| `gatelevel_test_results` | `eae378222cc4d2b356ec47cc5215a741dc2b205799de5a3d7b6e094dd688221f` |
| `precheck_reports` | `d662d48967b359fc8c2ba089a4b514d37aff322da535edc128fc0827d036133c` |

Hashes of principal extracted files are:

| File | SHA-256 |
| --- | --- |
| GDSII | `447d2647d0a0a730c10701ef425e6a94d2d90aaa3bc2deeaa544e33d0c796455` |
| OASIS | `304f7f164f7f4da1c1cca458c3080f598c27a4db4eda20c6987836a7f5a1c31f` |
| Gate-level Verilog | `6fe876bb868e570f1ea7c67b5479232e491d0b66a96558eb6985a04b8dc41c30` |
| Nominal SPEF | `72c5abf15a0175a6f4d36ee074af48b35f1ffb6d001394294550e490daf39f85` |
| Final metrics JSON | `d4968282f231b637ee4c0b4c3c290a06e784abcec695d77154eeab5d616e5318` |
| GDS render PNG | `d058e2891134e08ad116ff75160dd642694ab73b15809ca1422053c2a877d3bc` |

## Cost boundary

The project uses two digital tiles. Tiny Tapeout's current SKY130 rate is
EUR 70 per tile, so silicon area is EUR 140. A development kit, taxes, and
shipping are additional. The live calculator is:
<https://app.tinytapeout.com/calculator?pcbs=0&tiles=2>.
