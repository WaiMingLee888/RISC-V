## How it works

NanoV is a small, bit-serial RV32E RISC-V processor. One core operation is
performed over 32 input-clock cycles, which keeps the logic compact. This
SKY130/LibreLane build preserves the original `1x2` Tiny Tapeout footprint.
Instructions and data live in an external SPI RAM; there is no on-chip
instruction or data cache.

This project updates Michael Bell's silicon-proven Tiny Tapeout 4 NanoV design
to the current Tiny Tapeout SKY130 template. It keeps the pinned NanoV RTL used
for TT04. Two hand-instantiated SKY130 cells are expressed as equivalent generic
RTL so the same source is portable and fully synthesizable by the current flow.

The memory-mapped peripherals are:

| Address | Operation |
| --- | --- |
| `0x10000000` | Read or write the eight dedicated GPIO outputs |
| `0x10000004` | Read the eight dedicated GPIO inputs |
| `0x10000010` | Read or write one UART byte |
| `0x10000014` | UART status: bit 1 is RX valid, bit 0 is TX busy |

The UART is configured for 93,750 baud from a 12 MHz Tiny Tapeout clock. It has
no transmit or receive FIFO, so software must poll the status register.

Important RV32E restrictions inherited from NanoV:

- `x3/gp` is fixed at `0x00001000`.
- `x4/tp` is fixed at `0x10000000`.
- Interrupts and `ebreak` are not implemented.

## How to test

Run the integration regression from the repository root:

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r test/requirements.txt
cd test
make -B
! grep failure results.xml
```

The test boots the supplied program image from the simulated SPI RAM and
checks UART echo, inverted echo, byte addition, GPIO I/O, 32-bit multiply, and
64-bit multiply. The upstream NanoV ALU, core, CPU, and wrapper regressions are
also documented in `UPSTREAM.md`.

On hardware, hold `rst_n` low while programming the external SPI RAM. Release
reset, provide a 12 MHz clock, and observe the UART or GPIO outputs.

## External hardware

- An SPI RAM compatible with the `0x03` read and `0x02` write commands, or
  Michael Bell's RP2040 SPI-RAM emulator
- A 93,750-baud UART adapter for console I/O
- Optional LEDs or a seven-segment display on `uo[7:0]`

## Attribution

The CPU and original Tiny Tapeout wrapper are by Michael Bell and are licensed
under Apache-2.0. The UART blocks are MIT-licensed work by Ben Marshall, with
changes by Michael Bell. Exact source commits, retained licenses, and migration
changes are recorded in `UPSTREAM.md`.
