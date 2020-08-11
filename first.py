# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 13:34:53 2020

@author: USER
"""

#FHGJUJTJYTUIGYUGUUYUYF6D
from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

time.sleep(1)
x,y,z=mc.player.getTilePos()

#x=310
#y=69
#z=95
#i=0

#print(mc.player.getTilePos())
#mc.player.setPos(50,100,100)
#while i<10:
    #mc.setBlock(x,y,z,20)
    #y=y+1
    #i=i+1
mc.setBlock(x,y-1,z,20)
mc.setBlock(x+1,y-1,z,20)
mc.setBlock(x+1+1,y-1,z,20)
mc.setBlock(x+1+1,y-1,z-1,20)
mc.setBlock(x+1+1,y-1,z-1-1,20)
mc.setBlock(x+1,y-1,z-1-1,20)
mc.setBlock(x,y-1,z-1-1,20)
mc.setBlock(x,y-1,z-1,20)
