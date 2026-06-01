import serial
import time
import os
from dotenv import load_dotenv

load_dotenv()

# get variables from env file
port = os.getenv('SERIAL_PORT')
baud_rate = int(os.getenv('BAUD_RATE'))

def dispense_food():
    try:
        # initialize and open port for arduino
        with serial.Serial(port,baud_rate,timeout=2) as arduino:
            # add delay
            time.sleep(2)
            # write to arduino
            arduino.write(b'DISPENSE\n')
    except serial.SerialException as e:
        print(f"serial error: {e}")

if __name__ == "__main__":
    dispense_food() 