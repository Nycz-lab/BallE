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
import _thread
import socket
import json



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

        #network interface config
        self.address = "127.0.0.1" #localhost
        self.port = 5555
        self.handshake_msg = "BallE_client"
        self.buff_size = 1024

        self.debugInfo = {

            "name": "BallE"

        }

        # dynamic init happens here:
        self.initMedia()

        _thread.start_new_thread(self.broadcast, ())

    def padString(self, msg, padSize):  # adds padding of size padSize to string
        return msg + (padSize - len(msg)) * '\0'

    def broadcast(self):    # network interface stuff definitely not written by nick

        addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        addr.connect((self.address, self.port))
        
        msg = self.handshake_msg
        padded_msg = self.padString(msg, self.buff_size)
        addr.send(padded_msg.encode())

        while True: # TODO find a better way to handle this

            self.debugInfo["rotation"] = self.gyro.angle()

            json_obj = json.dumps(self.debugInfo)

            addr.send(self.padString(json_obj, self.buff_size).encode())
            
            time.sleep(1.5)
            

    def initMedia(self): # TODO no hardcoded strings
        for file in os.listdir("/home/robot/media"):
            self.soundNames.append("/home/robot/media/{}".format(file))

    def batteryCheck(self): # TODO this is very inaccurate
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


balle.batteryCheck()
#balle.playSoundRandom()


def test():
    #test for A8 and 16
    balle.turn_acc(75)
    balle.arm_rotate(400,400)
    balle.move(725)
    #wall down
    balle.arm_rotate(-400,400)
    balle.move(-100)
    balle.turn_acc(-65)
    balle.move(550)
    balle.turn_acc(80)
    balle.arm_rotate(400,400)
    balle.move(330)
    #crane is moved
    balle.arm.stop()

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

def station_a07():  # crane station
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
#test()
#station_a07()
#station_a08()
#station_a05()

while True:
    pass