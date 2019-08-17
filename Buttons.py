import RPi.GPIO as GPIO
import keyboard

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(32, GPIO.IN,pull_up_down=GPIO.PUD_UP)

#while True:
#    L = GPIO.input(6)
#    if (L == False):
#       keyboard.press('space')
#    else:
#       keyboard.release('space')