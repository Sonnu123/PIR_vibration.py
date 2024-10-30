#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# Define GPIO pins
BuzzerPin = 11   # Buzzer connected to pin 11
MotionPin = 12   # PIR motion sensor connected to pin 12

def setup():
    GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering

    # Setup Buzzer
    GPIO.setup(BuzzerPin, GPIO.OUT)
    GPIO.output(BuzzerPin, GPIO.HIGH)  # Initialize buzzer to off

    # Setup PIR Motion Sensor
    GPIO.setup(MotionPin, GPIO.IN)

def on():
    GPIO.output(BuzzerPin, GPIO.LOW)  # Turn buzzer on

def off():
    GPIO.output(BuzzerPin, GPIO.HIGH)  # Turn buzzer off

def beep(duration):
    on()
    time.sleep(duration)
    off()
    time.sleep(duration)

def loop():
    try:
        print("Waiting for PIR to stabilize...")
        time.sleep(10)  # Allow PIR sensor to stabilize
        print("PIR Ready!")
        while True:
            motion = GPIO.input(MotionPin)
            if motion == 1:
                print("Motion detected!")
                beep(0.5)  # Beep for 0.5 seconds
            else:
                off()  # Ensure buzzer is off
            time.sleep(0.1)
    except KeyboardInterrupt:
        destroy()

def destroy():
    off()
    GPIO.cleanup()
    print('GPIO cleaned up and program exited')

if __name__ == '__main__':
    setup()
    loop()
