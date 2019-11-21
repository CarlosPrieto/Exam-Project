#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:40:37 2019

@author: margueritehuck
"""

import numpy as np
import math 

#https://thispointer.com/python-how-to-replace-single-or-multiple-characters-in-a-string/

def turtleGraph(LindenmayerString,N):
    turtleCommands=np.zeros(len(LindenmayerString))

               #Sierpinski
    if 'A' in LindenmayerString :
        LineLength=N/2
        for i in range (0,len(LindenmayerString)):
            if LindenmayerString[i]=='A':
                turtleCommands[i]=LineLength
            elif LindenmayerString[i]=='B':
                turtleCommands[i]=LineLength
            elif LindenmayerString[i]=='L':
                turtleCommands[i]=1/3* math.pi
            elif LindenmayerString[i]=='R':
                turtleCommands[i]=1/3* math.pi   
        
               #Koch
    elif 'S' in LindenmayerString :
        LineLength=N/3
        for i in range (0,len(turtleCommands)):
            if LindenmayerString[i]=='S':
                turtleCommands[i]=LineLength
            elif LindenmayerString[i]=='L':
                turtleCommands[i]=1/3* math.pi
            elif LindenmayerString[i]=='R':
                turtleCommands[i]=2/3*math.pi 
    return turtleCommands