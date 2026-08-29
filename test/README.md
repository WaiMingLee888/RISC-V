# NanoV integration regression

The cocotb test boots `test.mem` through `sim_spi_ram.v` and verifies UART,
GPIO, and multiply behavior through the Tiny Tapeout wrapper.

From this directory:

```sh
make -B
! grep failure results.xml
```

The legacy NanoV RTL elaborates with Icarus 11 or 12. Icarus 13 rejects several
upstream forward declarations, so the explicit local RTL command on this
laptop is:

```sh
ICARUS_BIN_DIR=/home/ai/ttsetup/iverilog11/usr/bin make -B
```

After a successful SKY130 hardening run has supplied `gate_level_netlist.v` and
`PDK_ROOT` points to the SKY130 PDK, run:

```sh
make -B GATES=yes
! grep failure results.xml
```

The Makefile loads the SKY130 HD primitives and functional cell models for the
gate-level run. After changing simulator versions or netlists, remove the old
build with `GATES=yes make clean` before rerunning.

The waveform is written to `tb.fst`.
