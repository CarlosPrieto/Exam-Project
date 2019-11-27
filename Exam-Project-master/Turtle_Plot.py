#Main contributor: Carlos

import math
import numpy as np
import matplotlib.pyplot as plt

def turtlePlot(turtleCommands, pattern, N):
    #Formatting into matrix size of point-coordinates
    plotPoints = np.zeros([int(turtleCommands.size/2)+1,2])
    direction = np.array([1,0])
    plotPoints[0] = np.array([turtleCommands[0],0])
    #Calculating said points
    for i in range (np.size(plotPoints,axis=0)-1):
        length = turtleCommands[2*i]
        ang = turtleCommands[2*i+1]
        direction = np.matmul(np.array([[math.cos(ang),-math.sin(ang)],[math.sin(ang),math.cos(ang)]]),direction) #From https://docs.scipy.org/doc/numpy/reference/generated/numpy.matmul.html
        plotPoints[i+1] = plotPoints[i] + length * direction
    #Adding start-point
    plotPoints = np.concatenate((np.array([[0,0]]),plotPoints),axis=0)
    
    #Plotting points, defining borders and title
    plt.plot(plotPoints[:,0],plotPoints[:,1])
    plt.xlim(0,1)
    if pattern == "Koch curve":
        plt.ylim(-0.225,0.525)
    if pattern == "Sierpinski triangle" and N!=0:
        plt.ylim(np.min(plotPoints[:,1]),np.max(plotPoints[:,1]))
    plt.title(pattern + " after {:d} iteration(s)".format(N))
    
    plt.show()    
    return