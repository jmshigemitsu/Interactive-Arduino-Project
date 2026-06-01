import serial

port = 'COM5'
baud_rate = 9600

def dispense_food():
    try:
        with serial.Serial(port,baud_rate,timeout=2) as arduino:
            arduino.write(b'DISPENSE\n')
    except serial.SerialException as e:
        print(f"serial error: {e}")

if __name__ == "__main__":
    dispense_food() 