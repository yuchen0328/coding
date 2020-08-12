# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:12:52 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
import buildPyramid
#import time
#import random
mc=Minecraft.create()

x,y,z = mc.player.getPos()

def buildPyram(x,y,z,base):
    height = (base//2)+1
    for i in range(height):
        x1 = x + i
        y1 = y + i
        z1 = z + i
        
        x2 = x + base - i
        
        z2 = z + base - i
        mc.setBlock(x1.y1,z1,x2,y,z2,24)

x,y,z = mc.player.getPos()    
buildPyramid(x,y,z,20)