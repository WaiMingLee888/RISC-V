# NanoV hardware bring-up

NanoV does not run Linux. It is an RV32E bare-metal processor without
interrupts, `ECALL`, privileged mode, or an MMU. This procedure boots the same
program image used by the RTL and extracted-netlist regressions, providing a
controlled first-silicon test before attempting custom firmware.

## Required hardware

- The fabricated shuttle chip on a compatible Tiny Tapeout demoboard
- Tiny Tapeout MicroPython firmware containing `ttboard` plus the
  NanoV-compatible `rp2.enable_sim_spi_ram()` extension
- A 3.3 V USB-to-UART adapter capable of 93,750 baud
- A common ground between the UART adapter and demoboard

Do not connect the UART adapter's 5 V pin. Connect adapter RX to NanoV
`uio[5]` (TX), adapter TX to `uio[4]` (RX), and ground to ground. `uio[6]` is
NanoV's active-low receive-ready signal and may be connected to CTS when the
adapter supports hardware flow control. The stock Tiny Tapeout firmware source
does not currently expose `enable_sim_spi_ram`; use the compatible firmware
used by the [original TT04 NanoV bring-up](https://github.com/MichaelBell/tt04-nanoV/tree/main/micropython),
or attach a command-compatible external SPI memory instead.

The RP2040 simulated memory supplies NanoV's SPI pins:

| Tiny Tapeout pin | NanoV function |
| --- | --- |
| `uio[0]` | SPI RAM MOSI |
| `uio[1]` | SPI RAM chip select, active low |
| `uio[2]` | SPI RAM clock |
| `uio[3]` | SPI RAM MISO |
| `uio[7]` | SPI RAM HOLD, active low |

## Prepare the known-good image

On the host computer, convert the verified Verilog memory image into the
little-endian byte stream seen by the SPI interface:

```sh
python bringup/mem_to_bin.py test/test.mem bringup/test.bin
```

Copy `bringup/test.bin`, `bringup/load_spi_ram.py`, and `bringup/tt_boot.py` to
the demoboard's MicroPython filesystem. For example, with `mpremote`:

```sh
mpremote fs cp bringup/test.bin :test.bin
mpremote fs cp bringup/load_spi_ram.py :load_spi_ram.py
mpremote fs cp bringup/tt_boot.py :tt_boot.py
```

The generated project selector will exist only after this repository has been
submitted to a shuttle and that shuttle's MicroPython project index is
installed on the board.

## Boot

Enter the board's MicroPython REPL and run:

```python
import tt_boot
tt_boot.boot("test.bin")
```

This loads the image while NanoV is inactive, selects
`tt_um_WaiMingLee888_nanov`, applies ten reset clocks, releases reset, and
starts the project clock at 12 MHz. The UART format is 93,750 baud, 8 data
bits, no parity, and one stop bit.

## First-silicon smoke test

Install the host dependency and run the test against the UART adapter:

```sh
python -m pip install -r bringup/requirements.txt
python bringup/host_smoke.py COM6
```

Replace `COM6` with the actual serial port. A passing run checks byte echo,
inverted echo, and byte addition using the same firmware protocol covered by
the RTL and gate-level tests. When `uio[6]` is connected to the adapter's CTS
input, add `--rtscts`; otherwise the test inserts a conservative delay between
the two unacknowledged addition operands.

To stop the clock and return the project to reset:

```python
tt_boot.stop()
```

## Failure isolation

1. Confirm the selected shuttle contains `tt_um_WaiMingLee888_nanov`.
2. Confirm the project clock is 12 MHz and `rst_n` is high after boot.
3. Check `uio[1]` for active-low SPI transactions and `uio[2]` for its clock.
4. Check that UART TX (`uio[5]`) idles high.
5. Verify the UART is exactly 93,750 baud, 8-N-1, at 3.3 V logic levels.
6. If SPI is active but UART remains silent, reconvert and reload `test.mem`.
7. If SPI is inactive, inspect project selection, reset, and clock before
   changing firmware or RTL.

For persistent operation, replace the RP2040 emulator with SPI FRAM or RAM
that implements commands `0x03` (read) and `0x02` (write), then program the
same byte image while NanoV is held in reset.
