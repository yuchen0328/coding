# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:06:25 2020

@author: USER
"""
from mcpi.minecraft import Minecraft

import time

import random

mc=Minecraft.create()

time.sleep(1)

x,y,z=mc.player.getTilePos()

#while True:
    #colour=random.randrange(0,16)
    #mc.setBlocks(x+25,y-1,z+25,x-25,y-1,z-25,95,colour)
   # time.sleep(0.5)
#eprint(random.randrange(0,100))
wallet_a=random.randrange(0,10)
wallet_b=random.randrange(0,10)

if wallet_a== 4 or wallet_a== 8:
    print(4,8)
    
total=wallet_a + wallet_b

if total>10:
   print("yes")

print(wallet_a)
print(wallet_b)