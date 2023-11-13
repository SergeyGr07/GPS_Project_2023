import serial


def main(port: str, rate: int) -> bool:
    try: 
        ser = serial.Serial(port, rate)
        print("Serial connection established.")

        file = open("output.json", "w")

        while True:

            line = ser.readline().decode().strip()

            print("Received:", line)

            file.write(line + "\n")
            return True

    except KeyboardInterrupt:
        file.close()
        return False
