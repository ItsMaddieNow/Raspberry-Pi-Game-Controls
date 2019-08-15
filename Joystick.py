#!/usr/bin/python
 
import spidev
import os
import time
import math
import keyboard
 
# Define Axis Channels (channel 3 to 7 can be assigned for more buttons / joysticks)
swt_channel = 0
vrx_channel = 1
vry_channel = 2
 
#Time delay, which tells how many seconds the value is read out
deadzoneradius = 50.0
 
# Spi oeffnen
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1350000

# Function for reading the MCP3008 channel between 0 and 7
def readChannel(channel):
  val = spi.xfer2([1,(8+channel)<<4,0])
  data = ((val[1]&3) << 8) + val[2]
  return data

# endless loop
while True:
  # Determine position
  vrx_pos = readChannel(vrx_channel)
  vry_pos = readChannel(vry_channel)
  center_x = 511
  center_y = 511
  
  # SW determine
  swt_val = readChannel(swt_channel)

  # output
  vry_pos_centered = vry_pos - center_y
  vrx_pos_centered = vrx_pos - center_x
  
  if vrx_pos != center_x:
      if vry_pos != center_y:
          joystick_angle = math.degrees(math.atan2(vry_pos_centered, vrx_pos_centered))
  dist = math.sqrt(vry_pos_centered * vry_pos_centered + vrx_pos_centered * vrx_pos_centered)
      
  if joystick_angle > -67.5:
      if joystick_angle < 67.5:
          if dist > deadzoneradius:
              keyboard.press("w")
  else:
      if joystick_angle < 67.5:
          keyboard.release("w")
  if joystick_angle > 22.5:
      if joystick_angle < 157.5:
          if dist > deadzoneradius:
              keyboard.press("d")
  else:
      if joystick_angle > 157.5:
          keyboard.release("d")
  if joystick_angle > -157.5:
      if joystick_angle < -22.5:
          if dist > deadzoneradius:
              keyboard.press("a")
  else:
      if joystick_angle > -22.5:
          keyboard.release("a")
  if joystick_angle > 157.5:
      if dist > deadzoneradius:
          keyboard.press("s")
  if joystick_angle < -157.5:
      if dist > deadzoneradius:
          keyboard.press("s")
  else:
      if joystick_angle < 157.5:
          keyboard.release("s")
  if dist < deadzoneradius:
      keyboard.release("s")
      keyboard.release("a")
      keyboard.release("w")
      keyboard.release("d")
  if swt_val <= 2:
      keyboard.press("shift")
  else:
      keyboard.release("shift")