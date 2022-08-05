#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time
import random
class BallE:

    def __init__(self):

        self.ev3 = EV3Brick()

        # Const Definition
        self.ballinSound = "ballin.wav"
        self.diameter = 57
        self.axes = 94

        # Motor Definition
        self.mr = Motor(Port.D)
        self.ml = Motor(Port.A)
        self.arm = Motor(Port.B)

        # Sensor Definition
        self.gyro = GyroSensor(Port.S1)
        self.trans = DriveBase(self.mr, self.ml, self.diameter, self.axes)

        #sound 
        speaker1 = self.ev3.speaker
        speaker1.set_volume(100)

    def arm_rotate(self, rotation, time):
        self.arm.run_time(rotation, time)

    def move(self, vel):
        self.trans.straight(vel)

    def dance(self):
        self.ev3.speaker.play_file(self.ballinSound)
        self.trans.turn(random.randrange(10, 360))
        self.trans.straight(random.randrange(10,100))

balle = BallE()

def stationA03():
    balle.arm_rotate(-500, 800)
    balle.arm_rotate(2000, 1000)
    balle.move(500)
    #balle.arm_rotate(35)

    balle.ev3.speaker.play_file("ballin.wav")
    #balle.ev3.speaker.say("Tom ran over a cat with a lawnmower and blamed it on somebody else")

stationA03()

""" 
while calibration != maxCalibrations:

    balle.gyro.reset_angle(0)

    balle.trans.turn(90)
    print(balle.gyro.angle())
    if balle.gyro.angle() == -90:
        calibration += 1
    else:

        calibration = 0
        if balle.gyro.angle() < -90:
            balle.axes += 1
        elif balle.gyro.angle() > -90:
            balle.axes -= 1
    


for i in range(0,9):
    print(balle.gyro.angle())
    balle.gyro.reset_angle(0)
    balle.trans.turn(90)
    print(balle.gyro.angle())
    print("---------------")
 """
#balle.trans.settings(100,100,10,10)

#maxCalibrations = 10

#calibration = 0
#while True:
#    balle.dance()
#balle.dev_run()

    #print(balle.arm.angle())
    #balle.arm.run_angle(1000, 90, wait=False)

#balle.ev3.speaker.say("Til Euter Knauts knows all the old scanners")