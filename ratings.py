#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 14:27:34 2020

@author: alexlaw
"""

from elopy import *

i = Implementation()

i.addPlayer("Hank",rating=1000)
i.addPlayer("Bill",rating=900)



i.recordMatch("Hank","Bill",winner="Hank")



i.recordMatch("Hank","Bill",winner="Bill")



i.recordMatch("Hank","Bill",draw=True)





