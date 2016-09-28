import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib
import math

def MatrixCreate(rows,columns):
    matrix = np.zeros((rows,columns), dtype='f')
    return matrix

def MatrixRandomize(v):
    for i in range(0,1):
        for j in range(0,50):
            
            v[i,j] = random.random()
    return v

def Fitness(v):
    average = 0
    for i in range(0,1):
        for j in range (0,50):
            average = average + v[i,j]
    average = average/50
    return average
            

def MatrixPerturb(p, prob):
    c = MatrixCreate(len(p),len(p[0]))
    for row in range(len(p)):
        for column in range(len(p[row])):
            c[row][column] = p[row][column]
            if prob > random.random():
                c[row][column] = random.random()  
    return c
def PlotVectorAsLine(fits):
    
    plt.plot(fits[0])
            
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.axis([0,5000,.4,1])
    plt.draw()
    
    
def main():
    neuronValues = MatrixCreate(50,10)
    for i in range(0,1):
        for j in range(0,10):
            neuronValues[i][j] = random.random()
    
    neuronPositions = MatrixCreate(2,10)
    angle = 0.0
    angleUpdate = 2 * math.pi/10
    for i in range(0,10):
        x = math.sin(angle)
        y = math.cos(angle)
        angle = angle + angleUpdate
        neuronPositions[0][i] = x
        neuronPositions[1][i] = y

    for i in range(0,10) :       
        plt.plot([neuronPositions[0][i]],[neuronPositions[1][i]],'ko',markerfacecolor = [1,1,1],markersize = 18)
    plt.axis([-1,1,-1,1])
    plt.show()

    synapses = MatrixCreate(10,10)
    for i in range(0,10):
        for j in range(0,10):
            synapses[i][j] = random.uniform(-1,1)
    ##print synapses
    for i in range(len(neuronPositions[0])):
        for j in range(len(neuronPositions[0])):
            ## w for fig 2d
            w = int(10*abs(synapses[i][j]))+1
            ##next 4 lines for fig 2c
            weight = [0,0,0]
            if (synapses[i][j] < 0):
                weight = [0.8,0.8,0.8]
            ##plt.plot([neuronPositions[0][i], neuronPositions[0][j]],[neuronPositions[1][i],neuronPositions[1][j]], color=weight, linewidth = w)


            ## for fig 2c plt.plot([neuronPositions[0][i], neuronPositions[0][j]],[neuronPositions[1][i],neuronPositions[1][j]], color=weight)

            ##plt.plot([neuronPositions[0][i], neuronPositions[0][j]],[neuronPositions[1][i],neuronPositions[1][j]], color=[0,0,0])
    for i in range(50):
        Update (neuronValues,synapses,i)
    matplotlib.pyplot.imshow(neuronValues, cmap=matplotlib.pyplot.cm.gray, aspect='auto', interpolation='nearest')
    plt.show()

def Update(neuronValues,synapses,i):
    if i !=0:
        for j in range(len(neuronValues[0])):
            temp = 0
            for k in range(len(neuronValues[0])):
                temp += synapses[j][k]*neuronValues[i-1][k]
            if temp <0:
                temp = 0
            if temp > 1:
                temp = 1
            neuronValues[i][j] = temp   
    return neuronValues
                    
    

main()
