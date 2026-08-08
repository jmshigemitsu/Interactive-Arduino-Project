import os
from dispenser import FoodDispenser
from dotenv import load_dotenv

load_dotenv()

def main():
    # get variables from env file
    port = os.getenv('SERIAL_PORT')
    baud_rate = int(os.getenv('BAUD_RATE'))

    dispenser = FoodDispenser(port,baud_rate)

    try:
        dispenser.connect()
        dispenser.dispense()
    finally:
        dispenser.disconnect()

if __name__ == "__main__":
    main() 