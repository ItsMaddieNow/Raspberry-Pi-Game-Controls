import rpi.gpio as GPIO
import keyboard

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(8, GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(8, GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(8, GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(8, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    L = GPIO.input(5)
    if (L == False):
       keyboard.press('e')
    else:
       keyboard.release('e')
    R = GPIO.input(7)
    if (R == False):
       keyboard.press('q')
    else:
       keyboard.release('q')
    Z = GPIO.input(8)
    if (Z == False):
       keyboard.press('esc')
    else:
       keyboard.release('esc')
    Dpad_UP = GPIO.input(10)
    if (Dpad_UP == False):
       keyboard.press('up arrow')
    else:
       keyboard.release('up arrow')
    Dpad_DOWN = GPIO.input(12)
    if (Dpad_DOWN == False):
       keyboard.press('down arrow')
    else:
       keyboard.release('down arrow')
    Dpad_LEFT = GPIO.input(11)
    if (Dpad_LEFT == False):
       keyboard.press('left arrow')
    else:
       keyboard.release('left arrow')
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
    