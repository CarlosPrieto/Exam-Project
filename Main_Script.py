import numpy as np
from Lindenmayer_Iteration import LindIter
from Turtle_Graphics import turtleGraph
from Turtle_Plot import turtlePlot

LindenmayerString = ""

while True:
    function = str(input("1. Choose system and iterations\n2. Generate Plots\n3. Quit\nChoose a function\n"))
    if function == "1":
        #Chech N > -1
        while True:
            try:
                N = int(input("Input number of iterations\n"))
                break
            except ValueError:
                print("\nPlease input an integer greater than or equal to 0")
        while True:
            System = str(input("1. Koch curve\n2. Sierpinski triangle\nChoose an option or type in the name of the system\n"))
            if System == "1" or str.lower(System) == "koch curve":
                LindenmayerString = LindIter("Koch",N)
                pattern = "Koch curve"
                break
            elif System == "2" or str.lower(System) == "sierpinski triangle":
                LindenmayerString = LindIter("Sierpinski",N)
                pattern = "Sierpinski triangle"
                break
            else:
                print("\nPlease choose a valid option")
            
    elif function == "2":
        if LindenmayerString != "":
            turtleCommands = turtleGraph(LindenmayerString,N)
            turtlePlot(turtleCommands,pattern)
            
        else:
            print("\nPlease choose a system and number of iterations first")
        
    elif function == "3":
        break
    
    else:
        print("\nPlease choose an avaliable option")
        
        