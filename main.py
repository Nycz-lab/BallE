#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time
import random

import os

class BallE:

    def __init__(self):

        self.ev3 = EV3Brick()

        # Const Definition
        self.soundNames = []
        self.ballinSound = "ballin.wav"
        self.diameter = 57
        self.axes = 94

        # Battery
        self.battery_max = 9000                             # max battery voltage in millivolt
        self.battery_current = self.ev3.battery.voltage()   # current battery voltage in millivolt

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

        # dynamic init happens here:
        self.initMedia()

    def initMedia(self): #todo no hardcoded strings
        for file in os.listdir("/home/robot/media"):
            self.soundNames.append("/home/robot/media/{}".format(file))

    def batteryCheck(self):
        charge = balle.get_charge()
        if(charge < 0.2):
            print("Warning low battery!")
        print("battery is at {:.2f}%".format(charge * 100))

    def get_charge(self):
        return self.battery_current / self.battery_max

    def arm_rotate(self, rotation, time):
        self.arm.run_time(rotation, time)

    def turn(self, rotation):
        self.trans.turn(rotation)

    def playSoundRandom(self):
        soundIndex = random.randint(0, len(balle.soundNames) -1)
        balle.speaker.play_file(balle.soundNames[soundIndex])

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

    def move(self, vel):
        self.trans.straight(vel)

    def dance(self):
        self.ev3.speaker.play_file(self.ballinSound)
        self.trans.turn(random.randrange(10, 360))
        self.trans.straight(random.randrange(10,100))

balle = BallE()

balle.batteryCheck()


def station3_5():
    #station 3 move arm of the Airplain 
    balle.move(500)
    balle.turn_acc(-45)
    balle.arm_rotate(300,800)
    balle.arm_rotate(-350,800)
    #station 5 move the arm of the engine 
    balle.move(-50)
    balle.turn_acc(90)
    balle.arm_rotate(400,600)
    balle.move(255)
    balle.arm_rotate(-300,600)
    balle.move(-750)


def station6_7_14left():
    balle.move(180)
    balle.turn_acc(90)
    balle.arm_rotate(250,500)
    balle.move(750)
    balle.turn_acc(-85)
    balle.move(430)
    balle.turn_acc(90)
    balle.move(300)
    balle.move(-250)
    balle.arm_rotate(-250,500)
    balle.turn_acc(-130)
    balle.arm_rotate(250,500)

#station3_5()
station6_7_14left()
#station6_7_8_14()
balle.playSoundRandom()