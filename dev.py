#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
# Create your objects and variables here.

def debugTurn():
    
    #wheels.straight(200)
    gyro.reset_angle(0)
    #wheels.turn(90)
    #ev3.speaker.play_file("ballin.wav")
    while gyro.angle() != 90:
        print(gyro.angle())
        if gyro.angle() < 90:
            wheels.turn(1)
        if gyro.angle() > 90:
            wheels.turn(-1)

ev3= EV3Brick()

# Write your program here.
m1 = Motor(Port.A)
m2 = Motor(Port.D)
#gyro = GyroSensor(Port.S1)
gyro2 = GyroSensor(Port.S2)

ev3.speaker.set_speech_options(language="ru", voice="m3", speed=.5, pitch=.5)
#ev3.speaker.say("ballin")
#ev3.speaker.say("cyka blyat")
ev3.speaker.set_volume(100)
ev3.speaker.play_file("ballin.wav")

#ev3.speaker.beep()
#while True:
#    print(g.angle())
#    print("\n")
#m.run_angle(1000, 360*4)

wheels = DriveBase(m1, m2, 60, 90)
#debugTurn()
print(gyro2.angle())
wheels.turn(90)
#print("First reported: ")
#print(gyro.angle())
print("Second reported: ")
print(gyro2.angle())
print((gyro.angle() + gyro2.angle()) / 2)


#print(gyro.angle())