# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:20:38 2020

@author: USER
"""

from mcpi.minecraft import Minecraft
#import time
import random

mc=Minecraft.create()
"""
a = random.randrange(0,50)
b = random.randrange(0,50)
c = random.randrange(0,50)
"""
a=10
b=3
c=9
Lista = [a,b,c]
Lista[0]
Lista[1]
Lista[2]
print(Lista)

if b > a:
    t = a
    a = b
    b = t
if c > b:
    t = b
    b = c
    c = t
if b > a:
    t = a
    a = b
    b = t
print(Lista)

