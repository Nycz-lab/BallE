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
        self.touch = TouchSensor(Port.S2)
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
        i=0
        while(self.gyro.angle() != rotation):
            i = i + 1
            if i > 10:
                break
            difference = rotation - self.gyro.angle()
            turn_rate = (difference * 0.5)*-1
            if turn_rate < 0 and turn_rate > 1:
                self.trans.turn(1)
            elif turn_rate < 0 and turn_rate > -1:
                self.trans.turn(-1)
            else:
                self.trans.turn(turn_rate)
        self.trans.stop()
        self.trans.reset()

    def move(self, vel, drive_speed=150, turn_rate=0):
        while self.trans.distance() <= vel:
            self.trans.drive(drive_speed, turn_rate)
        self.trans.stop()
        print(self.trans.distance())
        self.trans.reset()

    def dance(self):
        self.ev3.speaker.play_file(self.ballinSound)
        self.trans.turn(random.randrange(10, 360))
        self.trans.straight(random.randrange(10,100))

balle = BallE()
def station3_5():
    #station 3 move arm of the Airplain
    balle.move(500)
    balle.turn_acc(-45)
    balle.arm_rotate(300,800)
    balle.arm_rotate(-350,800)
    #station 5 move the arm of the engine
    balle.move(-50)
    balle.turn_acc(89)
    balle.arm_rotate(400,600)
    balle.move(255)
    balle.arm_rotate(-300,600)
    balle.move(-750)

def station8_9_14():
    #station 8 helicopter
    balle.turn_acc(65)
    balle.move(889)
    balle.turn_acc(86)
    balle.move(800)
    balle.turn_acc(-3)
    balle.move(245)
    balle.turn_acc(86)
    balle.move(88)
    #station 9 rail down
    balle.trans.straight(-170)
    balle.turn_acc(0)
    balle.move(150)
    while balle.touch.pressed()!=True:
        balle.move(20)
    print(balle.gyro.angle())
    balle.gyro.reset_angle(0)
    balle.trans.straight(-650)
    balle.turn_acc(90)
    balle.move(160)
    balle.arm_rotate(300,500)
    balle.trans.straight(-150)
    balle.arm_rotate(-300,520)
    #station 14 wall right down
    balle.trans.straight(-380)
    #back to base

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


balle.batteryCheck()
balle.gyro.reset_angle(0)
#station3_5()
station8_9_14()
#station6_7_14left()
balle.trans.stop()
balle.playSoundRandom()