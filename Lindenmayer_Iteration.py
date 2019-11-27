# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:50:20 2019

@author: Nico1
"""

def LindIter(System,N):
    if System == "Koch":
        LindenmayerString = "S"
        for i in range (0,N):
            LindenmayerString = LindenmayerString.replace("S","SLSRSLS")
    
    elif System == "Sierpinski":
        LindenmayerString = "A"
        #Iterating LindenmayerString N times. tempString is LindenmayerString from i-1 iteration
        for i in range (0,N):
            tempString = LindenmayerString
            LindenmayerString = ""
            #Checking each letter q in tempString and replacing it accordingly in LindenmayerString
            for q in range (0,len(tempString)):
                if tempString[q] == "A":
                    LindenmayerString += "BRARB"
                elif tempString[q] == "B":
                    LindenmayerString += "ALBLA"
                elif tempString[q] == "L":
                    LindenmayerString += "L"
                elif tempString[q] == "R":
                    LindenmayerString += "R"
    
    return LindenmayerString