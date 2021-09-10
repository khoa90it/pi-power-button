#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess

pinLed = 3
pinFan = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLed, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(pinLed, GPIO.FALLING)

GPIO.setup(pinFan, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(pinFan, GPIO.FALLING)

subprocess.call(['shutdown', '-h', 'now'], shell=False)
