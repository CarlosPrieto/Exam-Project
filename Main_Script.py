import numpy as np
from Lindenmeyer_Iteration import LindIter
from Data_Statistics import dataStatistics
from Turtle_Plot import turtlePlot

while True:
    function = str(input("1. Choose system and iterations\n2. Generate Plots\n3. Quit\nChoose a function\n"))
    if function == "1":
        System = str(input("1. Koch curve\n2. Sierpinski triangle\nChoose an option or type in the name of the system\n"))
        try:
            N = int(input("Input nubmer of iterations"))
            break
        except ValueError:
            print("Please input an integergreater than 0")
            
    if function == "2":
        LindIter(System,N)
        
    if function == "3":
        break
    else:
        print("\nPlease choose an avaliable option")