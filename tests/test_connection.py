import os

import pytest
from dotenv import load_dotenv

from dispenser import FoodDispenser

load_dotenv()

@pytest.fixture
def dispenser():
    port = os.getenv("SERIAL_PORT")
    baud_rate = int(os.getenv("BAUD_RATE", "9600"))

    dispenser = FoodDispenser(port, baud_rate)

    dispenser.connect()

    try:
        yield dispenser
    finally:
        dispenser.disconnect()


def test_arduino_ping_returns_pong(dispenser):
    assert dispenser.ping() is True
