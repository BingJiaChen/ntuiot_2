#!/bin/python3
import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8,GPIO.OUT)
    print("OK")

def blink():
    while True:
        GPIO.output(8,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(8,GPIO.LOW)
        time.sleep(0.5)

if __name__=="__main__":
    setup()
    blink()
