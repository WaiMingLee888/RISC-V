# NanoV RV32E for current Tiny Tapeout SKY130

This repository packages the silicon-proven NanoV bit-serial RISC-V core in
the current Tiny Tapeout SKY130 Verilog template. The physical build targets
`1x2` tiles, external SPI RAM for instructions and data, and exposes GPIO plus a
93,750-baud UART when clocked at 12 MHz.

The submission top is `tt_um_WaiMingLee888_nanov`, matching the repository
owner's GitHub username.

## Verification

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r test/requirements.txt
cd test
make -B
! grep failure results.xml
```

The hosted RTL job uses Ubuntu 24.04 and Icarus. See `test/README.md` for the
local RTL and SKY130 gate-level commands used on this laptop.

The current Tiny Tapeout GitHub workflows run RTL tests, SKY130 hardening,
precheck, gate-level simulation, and the GDS viewer. A local RTL pass does not
by itself prove placement, routing, timing, DRC, or LVS; require the GDS and
precheck workflows to pass before submission.

The original TT04 silicon used `1x2`; this repository retains that footprint to
keep the silicon-area price to two Tiny Tapeout digital tiles.

## Verification status

The source was copied from the locally signed-off IHP port, but SKY130 physical
signoff is technology-specific. Do not submit until this repository's RTL,
gate-level, hardening, timing, DRC, LVS, antenna, and Tiny Tapeout precheck gates
all pass. Generated `tt_submission` files are ignored because the workflow
regenerates them from source.

- [Project datasheet](docs/info.md)
- [Exact upstream provenance and changes](UPSTREAM.md)
- [Tiny Tapeout local hardening guide](https://www.tinytapeout.com/guides/local-hardening/)
- [Original TT04 NanoV project](https://github.com/MichaelBell/tt04-nanoV)
- [NanoV core](https://github.com/MichaelBell/nanoV)

## License

Apache-2.0. The UART source has its own retained MIT license at
`src/nanoV/uart/LICENSE`.
