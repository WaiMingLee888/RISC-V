"""Load a binary into the Tiny Tapeout RP2040 simulated SPI RAM."""

import machine


SPI_RAM_BASE = 0x20030000
SPI_RAM_LIMIT = 0x2003FC00


def load_spi_ram(filename):
    address = SPI_RAM_BASE
    with open(filename, "rb") as image:
        while True:
            data = image.read(1024)
            if not data:
                break
            if address + len(data) > SPI_RAM_LIMIT:
                raise ValueError("boot image exceeds the RP2040 simulated-RAM window")
            for value in data:
                machine.mem8[address] = value
                address += 1
            print(".", end="")
    print()
    print("Loaded %d bytes" % (address - SPI_RAM_BASE))
