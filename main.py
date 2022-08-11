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

def station3_4_5():
    #station 3
    balle.move(500)
    balle.turn_acc(-48)
    balle.arm_rotate(450,500)
    balle.arm_rotate(-350,800)
    #station 4
    balle.move(-70)
    balle.turn_acc(88)
    balle.move(260)
    balle.turn_acc(75)
    balle.move(100)
    balle.turn_acc(-20)
    balle.move(60)
    balle.arm_rotate(400,700)
    balle.move(-150)
    balle.arm_rotate(-400,700)
    balle.move(-100)
    #station 4
    balle.turn_acc()
    balle.move()
    balle.arm_rotate(300,500)
    balle.move(-0)
    balle.arm_rotate(-300,500)
    balle.turn_acc()
    balle.move()
    balle.arm_rotate(300,500)
    balle.move(-0)
    balle.arm_rotate(-300,500)
    #back to base
    balle.turn_acc()
    balle.move()

def station6_7_8_14():
    balle.move()

def station10_9():
    #box grün
    balle.move()
    balle.turn_acc(90)
    balle.move()
    balle.trun_acc(90)
    balle.move()
    balle.arm_rotate(300,400)
    balle.move(-200)
    #box blue
    balle.arm_rotate(-300,400)
    balle.trun_acc(-90)
    balle.move()
    #station 9 gleise
    balle.turn_acc(90)
    balle.arm_rotate(300,400)
    balle.move()
    balle.arm_rotate(-300,400)
    balle.turn_acc(-90)
    balle.move()
    balle.arm_rotate(150,400)
    #station 14 right 
    balle.move(-0)
    balle.turn_acc(180)
    balle.move()
    #back
    balle.turn_acc(90)
    balle.move()
    balle.turn_acc(-90)
    balle.move()
    balle.turn_acc(-90)
    balle.move()

station3_4_5()
#station10_9()
#station6_7_8_14()