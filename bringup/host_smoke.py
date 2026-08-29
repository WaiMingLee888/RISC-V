#!/usr/bin/env python3
"""Exercise the first three commands implemented by NanoV's test image."""

from __future__ import annotations

import argparse
import time

import serial


def exchange(port: serial.Serial, value: int) -> int:
    port.write(bytes([value]))
    response = port.read(1)
    if len(response) != 1:
        raise TimeoutError(f"no UART response after sending 0x{value:02x}")
    return response[0]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("port", help="serial port, for example COM6 or /dev/ttyUSB0")
    parser.add_argument(
        "--rtscts",
        action="store_true",
        help="use hardware flow control when NanoV uio[6] is wired to adapter CTS",
    )
    parser.add_argument(
        "--inter-byte-delay",
        type=float,
        default=0.01,
        help="delay between unacknowledged bytes without flow control (default: 0.01 s)",
    )
    args = parser.parse_args()

    with serial.Serial(args.port, 93750, timeout=2, rtscts=args.rtscts) as uart:
        time.sleep(0.1)
        first = 0x35
        actual = exchange(uart, first)
        assert actual == first, f"echo: expected 0x{first:02x}, got 0x{actual:02x}"

        second = 0xA6
        actual = exchange(uart, second)
        expected = second ^ 0xFF
        assert actual == expected, f"invert: expected 0x{expected:02x}, got 0x{actual:02x}"

        a, b = 0x29, 0x53
        uart.write(bytes([a]))
        if not args.rtscts:
            time.sleep(args.inter_byte_delay)
        uart.write(bytes([b]))
        response = uart.read(1)
        if len(response) != 1:
            raise TimeoutError("no UART response from addition test")
        expected = (a + b) & 0xFF
        assert response[0] == expected, (
            f"add: expected 0x{expected:02x}, got 0x{response[0]:02x}"
        )

    print("PASS: NanoV UART echo, invert, and addition boot tests")


if __name__ == "__main__":
    main()
