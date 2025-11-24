# Write python script to continuously send commands ('ON' or 'OFF') to control an LED on Arduino

import serial
import time

arduino_port = 'COM7'
baud_rate = 9600

try:
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2) # Allow time for Arduino to reset
    print("LED control started. Press Ctrl+C to stop.")
    while True:
        ser.write(b'ON\n') # Send 'ON' command
        print("LED is ON")
        time.sleep(1)

        ser.write(b'OFF\n') # Send 'OFF' command
        print("LED is OFF")
        time.sleep(1)
except serial.SerialException as e:
    print(f"Serial error: {e}")
except KeyboardInterrupt:
    print("\nLED control stopped.")
    ser.close()

# Arduino Code (LED_Control.ino):
const int ledPin = 13;
void setup() {
    pinMode(ledPin, OUTPUT); // Set LED pin as output
    Serial.begin(9600); // Initialize serial communication
}

void loop() {
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n');
        command.trim(); // Remove any whitespace
        if (command == "ON") {
            digitalWrite(ledPin, HIGH); // Turn LED on
        } else if (command == "OFF") {
            digitalWrite(ledPin, LOW); // Turn LED off
        }
    }
}
            