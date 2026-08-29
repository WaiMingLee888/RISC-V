#!/usr/bin/env python3
"""Host-side unit tests for NanoV image preparation and board sequencing."""

from __future__ import annotations

import importlib
import sys
import tempfile
import types
import unittest
from pathlib import Path

BRINGUP_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BRINGUP_DIR))

from mem_to_bin import convert


class ImageConversionTests(unittest.TestCase):
    def test_readmemh_words_become_little_endian_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory, "program.mem")
            destination = Path(directory, "program.bin")
            source.write_text("008080e8 // first instruction\n12345678\n", encoding="ascii")

            self.assertEqual(convert(source, destination), 8)
            self.assertEqual(
                destination.read_bytes(),
                bytes.fromhex("e880800078563412"),
            )

    def test_invalid_word_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory, "bad.mem")
            destination = Path(directory, "bad.bin")
            source.write_text("1234\n", encoding="ascii")
            with self.assertRaisesRegex(ValueError, "expected one 32-bit"):
                convert(source, destination)


class BoardBootTests(unittest.TestCase):
    def tearDown(self) -> None:
        sys.modules.pop("tt_boot", None)

    def test_boot_loads_memory_before_select_reset_and_clock(self) -> None:
        events: list[object] = []

        class FakePin:
            PULL_UP = "pull-up"

        class FakeProject:
            def enable(self) -> None:
                events.append("enable")

        class FakeUio:
            pull = None

        class FakeBoard:
            def __init__(self) -> None:
                self.shuttle = types.SimpleNamespace(
                    tt_um_WaiMingLee888_nanov=FakeProject()
                )
                self.uio1 = FakeUio()

            def reset_project(self, asserted: bool) -> None:
                events.append(("reset", asserted))

            def clock_project_once(self) -> None:
                events.append("clock-once")

            def clock_project_PWM(self, frequency: int) -> None:
                events.append(("pwm", frequency))

        board = FakeBoard()
        fake_rp2 = types.ModuleType("rp2")
        fake_rp2.enable_sim_spi_ram = lambda: events.append("spi-enable")
        fake_machine = types.ModuleType("machine")
        fake_machine.Pin = FakePin
        fake_demoboard = types.ModuleType("ttboard.demoboard")
        fake_demoboard.DemoBoard = types.SimpleNamespace(get=lambda: board)
        fake_ttboard = types.ModuleType("ttboard")

        saved = {
            name: sys.modules.get(name)
            for name in ("rp2", "machine", "ttboard", "ttboard.demoboard")
        }
        try:
            sys.modules.update(
                {
                    "rp2": fake_rp2,
                    "machine": fake_machine,
                    "ttboard": fake_ttboard,
                    "ttboard.demoboard": fake_demoboard,
                }
            )
            tt_boot = importlib.import_module("tt_boot")
            tt_boot.load_spi_ram = lambda filename: events.append(("load", filename))
            tt_boot.boot("known-good.bin")
        finally:
            for name, module in saved.items():
                if module is None:
                    sys.modules.pop(name, None)
                else:
                    sys.modules[name] = module

        self.assertEqual(board.uio1.pull, FakePin.PULL_UP)
        self.assertEqual(events[:4], [("load", "known-good.bin"), "spi-enable", "enable", ("reset", True)])
        self.assertEqual(events.count("clock-once"), 10)
        self.assertEqual(events[-2:], [("reset", False), ("pwm", 12_000_000)])


if __name__ == "__main__":
    unittest.main()
