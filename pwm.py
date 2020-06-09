import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt


signvalues = []
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.output(12,1) #LSB
GPIO.output(15,0)
GPIO.cleanup()