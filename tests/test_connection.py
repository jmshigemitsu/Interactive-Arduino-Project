def test_arduino_ping_returns_pong(dispenser):
    assert dispenser.ping() is True
