# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:26:06 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
#import random

mc=Minecraft.create()

x,y,z = mc.player.getTilePos()
while True:
    mc.executeCommand("weather clear")
    time.sleep(5)
    mc.executeCommand("weather rain")
    time.sleep(5)