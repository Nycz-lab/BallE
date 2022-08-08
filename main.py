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

        # Battery
        self.battery = self.ev3.battery.voltage()

        # Motor Definition
        self.mr = Motor(Port.D)
        self.ml = Motor(Port.A)
        self.arm = Motor(Port.B)

        # Sensor Definition
        self.gyro = GyroSensor(Port.S1)
        self.trans = DriveBase(self.mr, self.ml, self.diameter, self.axes)

        #sound 
        self.speaker = self.ev3.speaker
        self.speaker.set_volume(100)

    def arm_rotate(self, rotation, time):
        self.arm.run_time(rotation, time)

    def turn(self, rotation):
        self.trans.turn(rotation)

    def nick(self, random):
        self.random = 1
    #nick

    def turn_acc(self, rotation):
        self.gyro.reset_angle(0)
        while True:
            if(self.gyro.angle() == 0):
                break

        while True:
            if(self.gyro.speed() == 0):
                break
        
        """
        Above is all calibration
        """

        while(self.gyro.angle() != rotation):
            difference = rotation - self.gyro.angle()
            turn_rate = (difference * 0.5)*-1
            if turn_rate < 1 and turn_rate > 0:
                self.trans.turn(1)
            elif turn_rate < 0 and turn_rate > -1:
                self.trans.turn(-1)
            else:
                self.trans.turn(turn_rate)

        self.trans.stop()

        print(self.gyro.angle())

    def move(self, vel):
        self.trans.straight(vel)

    def dance(self):
        self.ev3.speaker.play_file(self.ballinSound)
        self.trans.turn(random.randrange(10, 360))
        self.trans.straight(random.randrange(10,100))

    def square(self):
        balle.turn_acc(90)
        balle.move(300)
        balle.turn_acc(90)
        balle.move(300)
        balle.turn_acc(90)
        balle.move(300)
        balle.turn_acc(90)
        balle.move(300)

balle = BallE()

#print(balle.battery)

def station_a05():
    """
    station_a05 _summary_
    """
    balle.move(680)
    balle.turn_acc(70)
    balle.arm_rotate(500,400)
    balle.move(140)
    balle.arm_rotate(-200, 700)
    balle.ev3.speaker.play_file("ballin.wav")
    #balle.ev3.speaker.say("KUCKOKSMILSCH")
    #balle.ev3.speaker.say("Tom ran over a cat with a lawnmower and blamed it on somebody else")
    #turn back
    balle.move(-140)
    balle.turn_acc(-70)
    balle.move(-680)

def station_a07():
    balle.turn_acc(50)
    balle.move(1055)
    balle.turn_acc(38)
    balle.arm_rotate(450,400)
    balle.arm.hold()
    balle.move(200)
    balle.arm.stop()
    balle.ev3.speaker.play_file("ballin.wav")
    balle.move(-200)
    
def station_a08():
    balle.arm_rotate(-400, 400)
    balle.arm.stop()
    balle.turn_acc(25)
    balle.move(400)
    balle.turn_acc(-45)
    balle.move(500)


station_a07()
station_a08()
#station_a05()