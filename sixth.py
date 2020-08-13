# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 10:16:55 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
#import time
import random

mc=Minecraft.create()

x,y,z = mc.player.getTilePos()
for i in range(20):
    r=random.randrange(1,5)
    if r == 1:
        mc.setBlocks(x,y,z,x+4,y,z,1)
        x = x+4
    elif r == 2:
        mc.setBlocks(x,y,z,x-4,y,z,1)
        x = x-4
    elif r == 3:
        mc.setBlocks(x,y,z,x,y,z+4,1)
        z = z+4
    elif r == 4:
        mc.setBlocks(x,y,z,x,y,z-4,1)
        z = z-4
    else:
        mc.setBlocks(x,y,z,x,y+1,z,1)
        y = y+1
    
    
