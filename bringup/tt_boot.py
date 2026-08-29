"""Select, reset, and clock WaiMingLee888's NanoV Tiny Tapeout project."""

import rp2
from machine import Pin
from ttboard.demoboard import DemoBoard

from load_spi_ram import load_spi_ram


PROJECT_NAME = "tt_um_WaiMingLee888_nanov"
PROJECT_CLOCK_HZ = 12_000_000

tt = None


def boot(filename="test.bin"):
    """Load *filename* into simulated SPI RAM and release NanoV reset."""
    global tt
    if not hasattr(rp2, "enable_sim_spi_ram"):
        raise RuntimeError(
            "This firmware lacks rp2.enable_sim_spi_ram(); install the "
            "NanoV-compatible Tiny Tapeout MicroPython build"
        )
    load_spi_ram(filename)
    rp2.enable_sim_spi_ram()

    tt = DemoBoard.get()
    project = getattr(tt.shuttle, PROJECT_NAME)
    project.enable()

    # Keep the active-low SPI chip select deasserted while NanoV is reset.
    tt.uio1.pull = Pin.PULL_UP
    tt.reset_project(True)
    for _ in range(10):
        tt.clock_project_once()
    tt.reset_project(False)
    tt.clock_project_PWM(PROJECT_CLOCK_HZ)
    print("NanoV running at 12 MHz; UART is 93750 baud, 8-N-1")


def stop():
    """Stop the project clock and assert reset."""
    if tt is not None:
        tt.clock_project_stop()
        tt.reset_project(True)
