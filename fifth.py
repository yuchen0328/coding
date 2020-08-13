# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:20:01 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
#import time
#import random

mc=Minecraft.create()

x,y,z = mc.player.getPos()

line1 = []
for i in range(1,10):
    line1.append(1*i)

print(line1)

line2 = []
for i in range(1,10):
    line2.append(2*i)

print(line2)

line3 = []
for i in range(1,10):
    line3.append(3*i)

print(line3)
"""
line4 = []
for i in range(1,10):
    line4.append(4*i)

print(line4)

line5 = []
for i in range(1,10):
    line5.append(5*i)

print(line5)

line6 = []
for i in range(1,10):
    line6.append(6*i)

print(line6)

line7 = []
for i in range(1,10):
    line7.append(7*i)

print(line7)

line8 = []
for i in range(1,10):
    line8.append(8*i)

print(line8)

line9 = []
for i in range(1,10):
    line9.append(9*i)

print(line9)
"""

str(mc.setSign(x,y,z,63,0,str(line1),str(line2),str(line3)))