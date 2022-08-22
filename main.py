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

        #balle is born
        self.ev3 = EV3Brick()

        # Const Definition
        self.soundNames = []
        self.diameter = 57
        self.axes = 94
        self.rest = 10 #rest between stations in seconds

        # Battery
        self.batteryMax = 8307                            # max battery voltage in millivolt
        self.batteryCurrent = self.ev3.battery.voltage()   # current battery voltage in millivolt

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

        #dynamic init happens here:
        self.initMedia()

    def initMedia(self):
        for file in os.listdir("/home/robot/media"):
            self.soundNames.append("/home/robot/media/{}".format(file))

    def batteryCheck(self):
        charge = balle.get_charge()
        if(charge < 90):
            print("Warning low battery!")
        print("battery is at {:.2f}%".format(charge * 100))

    def get_charge(self):
        return self.batteryCurrent / self.batteryMax

    def arm_rotate(self, rotation, time):
        self.arm.run_time(rotation, time)

    def turn(self, rotation):
        self.trans.turn(rotation)

    def sound(self):
        soundIndex = random.randint(0, len(balle.soundNames) -1)
        balle.speaker.play_file(balle.soundNames[soundIndex])

    def turn_acc(self, rotation, turnForNTimes = 8):
        i=0
        while(self.gyro.angle() != rotation):
            i = i + 1
            if i > turnForNTimes:
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

    def move(self, vel, drive_speed=160, turn_rate=0):
        if drive_speed < 0:
            while self.trans.distance()*-1 <= vel:
                self.trans.drive(drive_speed, turn_rate)
        else:
            while self.trans.distance() <= vel:
                self.trans.drive(drive_speed, turn_rate)
        self.trans.stop()
        self.trans.reset()

    def dance(self):
        self.ev3.speaker.play_file(self.ballinSound)
        self.trans.turn(random.randrange(10, 360))
        self.trans.straight(random.randrange(10,100))

balle = BallE()

#!!!!!!!!!!!!!!!!!!!!!!!!!First Run!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def station8():
    #station 8 helicopter
    balle.turn_acc(65)
    balle.move(750,350)
    balle.turn_acc(92)
    balle.move(930,350)
    balle.turn_acc(0)
    balle.arm_rotate(270,600)
    balle.move(340,160)
    balle.turn_acc(40)
    balle.arm_rotate(-270,620)
    balle.turn_acc(90)
    balle.move(230,150)

def station9():
    #station 9 rail down
    balle.move(80, -100)
    balle.turn_acc(185)
    balle.move(465,150)
    balle.turn_acc(102)
    balle.move(90)
    balle.arm_rotate(280,500)
    balle.move(130, -150)
    balle.arm_rotate(-280,500)

def station14():
    #station 14 wall right down
    balle.turn_acc(270)
    balle.arm_rotate(250,500)
    balle.move(260,170)
    #station 14 wall left down
    balle.turn_acc(325)
    balle.move(230,170)
    balle.turn_acc(275)
    balle.move(270,170)
    balle.turn(150)

def backToBase1():
    #back to base 1
    balle.turn(-110)
    balle.arm_rotate(-300,550)
    balle.move(980,400)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!second Run!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def station3():
    #station 3 move arm of the Airplain
    balle.move(510)
    balle.turn_acc(-45)
    balle.arm_rotate(520,600)
    balle.arm_rotate(-520,600)

def station5():
    #station 5 move the arm of the engine
    balle.turn_acc(48)
    balle.arm_rotate(400,600)
    balle.move(225)
    balle.turn_acc(60,4)
    balle.arm_rotate(-300,800)
    balle.move(600,-350)
    balle.arm_rotate(-300,800)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!thirdRun!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def station12():
    balle.arm_rotate(365,500)
    time.sleep(3)
    balle.arm_rotate(-367,500)

def station7():
    #crane moved
    balle.turn_acc(54)
    balle.move(1090,150)
    balle.turn_acc(85)
    balle.arm_rotate(300,440)
    balle.move(240)

def station6():
    #wall down and stand
    balle.move(260,-180)
    balle.arm_rotate(-115,200)
    balle.turn_acc(-70)
    balle.move(105,80)

#!!!!!!!!!!!!!!!!All Runs!!!!!!!!!!!!!!

def check():
    print(balle.batteryCurrent)
    balle.batteryCheck()

def firstRun():
    balle.gyro.reset_angle(0)
    station8()
    station9()
    station14()
    backToBase1()

def secondRun():
    balle.gyro.reset_angle(0)
    station3()
    station5()

def thirdRun():
    balle.gyro.reset_angle(0)
    station7()
    station6()


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!start point!!!!!!!!!!!!!!!!!!!!!!!!!
#check battery and voltage
check()

#all Stations
#firstRun()
#secondRun()
#station12()
thirdRun()

#balle.sound()

#Stations done 3-30p, 5-20p, 6-30p, 7-30p, 8-20p, 9-20p, 12-30p, 14-20p
#together we will try to finish 8 Stations and to get 200 Points