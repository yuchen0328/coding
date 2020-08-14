# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:12:52 2020

@author: USER
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
x,y,z = mc.player.getTilePos() 

def buildPyramid(x,y,z,base):
    height = (base//2)+1
    for i in range(height):
        x1=x+i
        y1=y+i
        z1=z+i
        
        x2=x+base-i
        z2=z+base-i
        r = random.randrange(0,15)
        mc.setBlocks(x1,y1,z1,x2,y,z2,251,r)
x,y,z = mc.player.getTilePos()    
buildPyramid(x,y,z,20)
#金字塔