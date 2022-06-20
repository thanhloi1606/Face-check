import serial
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
try:
    while True:
        if (ser.in_waiting>0):
            print(ser.readline())