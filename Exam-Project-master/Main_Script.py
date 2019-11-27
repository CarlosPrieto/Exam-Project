from Lindenmayer_Iteration import LindIter #Written by Nicoline Hansen
from Turtle_Graphics import turtleGraph #Written by Marion Huck
from Turtle_Plot import turtlePlot #Written by Carlos Prieto
#The main script is written in equal colaboration between group members

LindenmayerString = ""

while True:
    function = str(input("1. Choose system and iterations\n2. Generate Plots\n3. Quit\nChoose a function:\n"))
    if function == "1":
        #Making sure that N is valid
        while True:
            try:
                N = int(input("Input number of iterations:\n"))
                if N >= 0:
                    break
                else:
                   print("\nPlease input an integer greater than or equal to 0")
            except ValueError:
                print("\nPlease input an integer greater than or equal to 0")
        #Choosing system and defining pattern for plot-name later
        while True:
            System = str(input("1. Koch curve\n2. Sierpinski triangle\nChoose an option or type in the name of the system:\n"))
            if System == "1" or str.lower(System) == "koch curve":
                LindenmayerString = LindIter("Koch",N)
                pattern = "Koch curve"
                break
            elif System == "2" or str.lower(System) == "sierpinski triangle":
                LindenmayerString = LindIter("Sierpinski",N)
                pattern = "Sierpinski triangle"
                break
            else:
                print("\nPlease choose a valid option (number or name)")
            
    elif function == "2":
        #Making sure that a Lindenmayer string has been defined, then generating plots
        if LindenmayerString != "":
            turtleCommands = turtleGraph(LindenmayerString,N)
            turtlePlot(turtleCommands,pattern,N)  
        else:
            print("\nPlease choose a system and number of iterations first")
        
    elif function == "3":
        break
    
    else:
        print("\nPlease choose an avaliable option")
        
        