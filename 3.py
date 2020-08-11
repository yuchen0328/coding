# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 16:15:57 2020

@author: USER
"""

from mcpi.minecraft import Minecraft

import time

#import random

mc=Minecraft.create()

time.sleep(1)

x,y,z=mc.player.getTilePos()

try:
    blockType=int(input("BLock id:"))
    mc.setBlock(x,y,z,blockType)
except:
    print("Invalid")
    