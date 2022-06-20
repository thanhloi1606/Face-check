import serial
from time import sleep

ser = serial.Serial('/dev/ttyACM0' , 9600)

try:
    while True:
        #nhan tin hieu tu arduino sang
        if (ser.in_waiting > 0):
            data = ser.readline()
            data = data.decode()
            data1 = data.rstrip()
            print(data1)
            sleep(1)
        #gui tin hieu tu python sang arduino
        else:
            string = "send 100 nghin"
            string1= string + "\r"
            ser.write(string1.encode())
            sleep(1)
expect KeyboardInterrupt
    ser.close()