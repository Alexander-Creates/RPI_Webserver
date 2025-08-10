#!/usr/bin/env python3
# /usr/lib/cgi-bin/gpio.py
import os
from urllib.parse import parse_qs
import sys

# HTTP header
print("Content-Type: text/plain")
print()

# parse query string: ?pin=17&state=1
qs = parse_qs(os.environ.get('QUERY_STRING',''))
try:
    pin = int(qs.get('pin',[''])[0])
    state = int(qs.get('state',[''])[0])  # 1 or 0
except Exception as e:
    print("error: missing/invalid parameters")
    sys.exit(0)

# control GPIO
try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH if state else GPIO.LOW)
    # Do not call cleanup() here if you want the state to remain.
    print(f"ok pin {pin} -> {state}")
except Exception as e:
    print("error:", e)
