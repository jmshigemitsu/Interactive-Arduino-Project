"""Shared pytest fixtures for tests that exercise the physical test bench."""

import os

import pytest
from dotenv import load_dotenv

from dispenser import FoodDispenser


load_dotenv()


@pytest.fixture
def dispenser():
    """Provide one connected dispenser and always release its serial port."""
    port = os.getenv("SERIAL_PORT")
    baud_rate = int(os.getenv("BAUD_RATE", "9600"))
    hardware = FoodDispenser(port, baud_rate)

    hardware.connect()
    try:
        yield hardware
    finally:
        hardware.disconnect()
