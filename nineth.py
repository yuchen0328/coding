# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:10:54 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
#import time
import random

mc=Minecraft.create()
for i in range(10):
    
    x,y,z = mc.player.getTilePos()
    
    y = y + i
    
    for i in range(10):
        
        r = random.randrange(0,16)
        
        z = z + 1
        
        mc.setBlock(x,y,z,35,r)
        