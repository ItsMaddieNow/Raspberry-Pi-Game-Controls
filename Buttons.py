import RPi.GPIO as GPIO
import keyboard

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(8, GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(8, GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(8, GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(8, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    L = GPIO.input(6)
    if (L == False):
       keyboard.press('space')
    else:
       keyboard.release('space')
    A = GPIO.input(25)
    if (A == False):
       keyboard.press('enter')
    else:
       keyboard.release('enter')
    R = GPIO.input(7)
    if (R == False):
       keyboard.press('e')
    else:
       keyboard.release('e')
    Z = GPIO.input(5)
    if (Z == False):
       keyboard.press('esc')
    else:
       keyboard.release('esc')
#    Dpad_UP = GPIO.input(21)
#    if (Dpad_UP == False):
#       keyboard.press('up arrow')
#    else:
#       keyboard.release('up arrow')
#    Dpad_DOWN = GPIO.input(12)
#    if (Dpad_DOWN == False):
#       keyboard.press('down arrow')
#    else:
#       keyboard.release('down arrow')
#    Dpad_LEFT = GPIO.input(11)
#    if (Dpad_LEFT == False):
#       keyboard.press('left arrow')
#    else:
#       keyboard.release('left arrow')
#    Z = GPIO.input(8)
#    if (Z == False):
#       keyboard.press('z')
#    else:
#       keyboard.release('z')
#    Z = GPIO.input(8)
#    if (Z == False):
#       keyboard.press('z')
#    else:
#       keyboard.release('z')
#    Z = GPIO.input(8)
#    if (Z == False):
#       keyboard.press('z')
#    else:
#       keyboard.release('z')
#    Z = GPIO.input(8)
#    if (Z == False):
#       keyboard.press('z')
#    else:
#       keyboard.release('z')
#    Z = GPIO.input(8)
#    if (Z == False):
#       keyboard.press('z')
#    else:
#       keyboard.release('z')
#    Z = GPIO.input(8)
#    if (Z == False):
#       keyboard.press('z')
#    else:
#       keyboard.release('z')
#    Z = GPIO.input(8)
#    if (Z == False):
#       keyboard.press('z')
#    else:
#       keyboard.release('z')
#    Z = GPIO.input(8)
#    if (Z == False):
#       keyboard.press('z')
#    else:
#       keyboard.release('z')
#    Z = GPIO.input(8)
#    if (Z == False):
#       keyboard.press('z')
#    else:
#       keyboard.release('z')
    