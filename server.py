#!/usr/bin/env python3

from flask import Flask
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

pin = 17

@app.route("/")
def open():
  GPIO.output(pin, GPIO.HIGH)
  time.sleep(4)
  GPIO.output(pin, GPIO.LOW)
  return "welcome"

def main():
  try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

    app.run(host="0.0.0.0", port=1312)
  finally:
    GPIO.cleanup()

if __name__ == "__main__":
  main()
