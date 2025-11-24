# Write a Python script to send a message from the PC to Arduino using PySerial.

import serial
import time

arduino = serial.Serial('COM7', 9600)
time.sleep(2) # Wait for Arduino to reset

while True:
    message = input("Type a message to send to Arduino: ")

    # Send message to Arduino
    arduino.write(message.encode())

    print("Message sent!\n")
    