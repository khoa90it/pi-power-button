#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess

pinLed = 3
pinFan = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(3, GPIO.FALLING)

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(2, GPIO.FALLING)

subprocess.call(['shutdown', '-h', 'now'], shell=False)
