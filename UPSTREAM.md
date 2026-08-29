# Upstream provenance

This port deliberately pins the RTL that was used by the silicon-proven Tiny
Tapeout 4 NanoV project.

| Component | Source | Pinned commit | License |
| --- | --- | --- | --- |
| Tiny Tapeout wrapper and integration test | `MichaelBell/tt04-nanoV` | `f6fcbbfe693fec80418b6dccc6447019cca8435e` | Apache-2.0 |
| NanoV CPU core | `MichaelBell/nanoV` | `8c95b70026e8878aa9e5a6c2f336890b25694fe7` | Apache-2.0 |
| UART RX/TX | Retained under `src/nanoV/uart` | Same pinned NanoV commit | MIT, Copyright 2021 Ben Marshall; changes Copyright 2023 Michael Bell |
| Tiny Tapeout project structure | `TinyTapeout/ttsky-verilog-template` | `60c39394fc4b67dd95e019ccd8849392eb00521d` | Apache-2.0 |

Retained license texts are in `LICENSE`, `src/nanoV/LICENSE`, and
`src/nanoV/uart/LICENSE`.

## Technology-port changes

Only two technology-specific RTL constructs were changed:

1. The Sky130 buffer on `spi_clk_enable` in `src/tt_top.v` became a direct
   continuous assignment.
2. The Sky130 scan-DFF accumulator in `src/nanoV/multiply.v` became NanoV's
   existing generic `reg` accumulator implementation.

The same two substitutions have precedent in Tiny Tapeout's historical IHP
NanoV integration and avoid binding functional RTL to a particular standard
cell. The wrapper was renamed to
`tt_um_WaiMingLee888_nanov`, metadata was migrated from YAML schema 4 to 6, the clock
was declared as 12 MHz, and the cocotb harness was updated for cocotb 2.x.

The silicon-proven TT04 project used `1x2`, and this SKY130 port retains that
footprint. Physical equivalence is not assumed: the current TTSKY26c flow must
independently pass placement, routing, timing, DRC, LVS, antenna, gate-level
simulation, and Tiny Tapeout precheck before submission.

No claim is made that this migration is a new CPU architecture. The purpose is
to provide a reproducible, attributed current-template ASIC project around an
existing working open-source RISC-V design.
