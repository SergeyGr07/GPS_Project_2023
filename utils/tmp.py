# Script for reqeuest
import serial
# Configure the COM port
port = "COM3"  # Replace with the appropriate COM port name
baudrate = 9600

try:
    # Open the COM port
    ser = serial.Serial(port, baudrate=baudrate)
    print("Serial connection established.")

    file = open("output.json", "w")

    # Read data from the Arduino
    while True:
        # Read a line of data from the serial port

        line = ser.readline().decode().strip()

        print("Received:", line)

        file.write(line + "\n")

except KeyboardInterrupt:
    file.close()
    pass
