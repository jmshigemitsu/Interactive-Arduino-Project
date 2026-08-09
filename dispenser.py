import serial
import time


class FoodDispenser:
    """Small Python interface for the Arduino food-dispenser protocol."""

    def __init__(self, port, baud_rate, timeout=20):
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.connection = None

    def connect(self):
        if not self.port:
            raise ValueError("SERIAL_PORT must be configured before connecting.")

        self.connection = serial.Serial(
            self.port, self.baud_rate, timeout=self.timeout
        )
        # Opening a serial connection resets many Arduino boards.  Give the
        # firmware time to finish setup before sending the first command.
        time.sleep(2)

    def disconnect(self):
        if self.connection and self.connection.is_open:
            self.connection.close()

    def dispense(self):
        response = self._send_command("DISPENSE")
        if response != "DISPENSE_OK":
            raise RuntimeError(f"Dispense failed: {response or 'no response'}")

        return True

    def ping(self):
        return self._send_command("PING") == "PONG"

    def _send_command(self, command):
        """Send one line-oriented command and return the Arduino response."""
        if not self.connection or not self.connection.is_open:
            raise RuntimeError("FoodDispenser is not connected.")

        self.connection.write(f"{command}\n".encode("ascii"))
        return self.connection.readline().decode("ascii", errors="replace").strip()
