# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 11:17:41 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
#import time
import random

mc=Minecraft.create()

#x,y,z = mc.player.getTilePos()
r=random.randrange(1,101)
print(r)
if r > 89:
    print("A+")
elif r < 90 and r > 79:
    print("A")
elif r < 80 and r > 69:
    print("B")
elif r < 70 and r > 59:
    print("C")
else:
    print("F")