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
        ifA = "BRARB"
        ifB = "ALBLA"
        ifL = "L"
        ifR = "R"
        for i in range (0,N):
            tempString = LindenmayerString
            LindenmayerString = ""
            for q in range (0,len(tempString)):
                if tempString[q] == "A":
                    LindenmayerString += ifA
                elif tempString[q] == "B":
                    LindenmayerString += ifB
                elif tempString[q] == "L":
                    LindenmayerString += ifL
                elif tempString[q] == "R":
                    LindenmayerString += ifR
    
    return LindenmayerString