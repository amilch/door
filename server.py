#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import RPi.GPIO as GPIO
import time

pin = 17

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Welcome!')
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(4)
        GPIO.output(pin, GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.LOW)

httpd = HTTPServer(('', 1312), SimpleHTTPRequestHandler)

try:
  httpd.serve_forever()
finally:
  GPIO.cleanup()

