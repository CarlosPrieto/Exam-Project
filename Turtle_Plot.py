#Main contributor: Carlos

import math
import numpy as np
import matplotlib.pyplot as plt

def turtlePlot(turtleCommands):
    plotPoints = np.zeros([int(turtleCommands.size/2),2])
    direction = np.array([1,0])
    for i in range (int(turtleCommands.size/2)):
        length = turtleCommands[2*(i+1)-2]
        ang = turtleCommands[2*(i+1)-1]
        direction = np.matmul(np.array([[math.cos(ang),-math.sin(ang)],[math.sin(ang),math.cos(ang)]]),direction) #From https://docs.scipy.org/doc/numpy/reference/generated/numpy.matmul.html
        plotPoints[i] = plotPoints[i-1] + length * direction
    plotPoints = np.concatenate((np.array([[0,0]]),plotPoints),axis=0)
    
    plt.plot(plotPoints[:,0],plotPoints[:,1])
    plt.xlim(np.min(plotPoints[:,0])-0.25,np.max(plotPoints[:,0])+0.25)
    plt.ylim(np.min(plotPoints[:,1])-0.25,np.max(plotPoints[:,1])+0.25)
#    plt.title()
    plt.show()    
    return

turtlePlot(np.array([1,math.pi/3,1,math.pi/3,1,-math.pi/3,1,-math.pi/3,1,-math.pi/3,1,-math.pi/3,1,math.pi/3,1,math.pi/3]))