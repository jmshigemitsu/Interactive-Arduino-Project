import serial
import time

class FoodDispenser:
    def __init__(self,port,baud_rate):
        self.port = port
        self.baud_rate = baud_rate
        self.connection = None

    def connect(self):
        self.connection = serial.Serial(self.port,self.baud_rate,timeout=20)
        time.sleep(2)

    def disconnect(self):
        if self.connection and self.connection.is_open:
            self.connection.close()

    def dispense(self):
        self.connection.write(b'DISPENSE\n')

        response = self.connection.readline().decode().strip()

        if response != "DISPENSE_CMD_OK":
            raise RuntimeError(f"Dispsense Failed: {response}")

    def ping(self):
        self.connection.write(b"PING\n")

        response = self.connection.readline().decode().strip()
        
        return response == "PONG"