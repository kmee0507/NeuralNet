import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib
import math

def MatrixCreate(rows,columns):
    matrix = np.zeros((rows,columns), dtype='f')
    return matrix


def VectorCreate(length):
    return np.zeros((length), dtype='f')

def MatrixRandomize(v):
    for i in range(len(v)):
        for j in range(len(v[i])):
            
            v[i,j] = random.random() * 2 - 1
    return v
def MatrixPerturb(p, prob):
    c = MatrixCreate(len(p),len(p[0]))
    for row in range(len(p)):
        for column in range(len(p[row])):
            c[row][column] = p[row][column]
            if prob > random.random():
                c[row][column] = random.random() * 2 - 1
    return c
def Update(neuronValues,synapses,i):
    
    for j in range(10):
        temp = 0
        for k in range(10):
##            print synapses[j,k]
##            print neuronValues[i,k]
##            print "hi"
            temp += synapses[j,k]*neuronValues[i,k]
        if temp <0:
            temp = 0
        if temp > 1:
            temp = 1
        neuronValues[i+1][j] = temp
    
    return neuronValues
def MeanDistance(v1,v2):
    total = 0
    for i in range(10):
        total += abs(v1[i] - v2[i])
    total = total / 10
    return total
def Fitness(v):
    neuronValues = MatrixCreate(10,10)
    for i in range(10):
        neuronValues[0,i] = 0.5
    
    for i in range(9):
        Update(neuronValues,v,i)
    
        
    #matplotlib.pyplot.imshow(neuronValues, cmap=matplotlib.pyplot.cm.gray, aspect='auto', interpolation='nearest')
    ##plt.show()
    actualNeuronValues = neuronValues[9,:]
    desiredNeuronValues = VectorCreate(10)
    for j in range(0,10,2):
        desiredNeuronValues[j] = 1
    d = MeanDistance(actualNeuronValues,desiredNeuronValues)
    return d

def Fitness2(v):
    neuronValues = MatrixCreate(10,10)
    for i in range(10):
        neuronValues[0,i] = 0.5
    
    for i in range(9):
        Update(neuronValues,v,i)
    
        
    #matplotlib.pyplot.imshow(neuronValues, cmap=matplotlib.pyplot.cm.gray, aspect='auto', interpolation='nearest')
    #plt.show()
    actualNeuronValues = neuronValues[9,:]
    desiredNeuronValues = VectorCreate(10)
    for j in range(0,10,2):
        desiredNeuronValues[j] = 1
    diff = 0.0
    for i in range(1,9): 

        for j in range(0,9):

            diff=diff + abs(neuronValues[i,j]-neuronValues[i,j+1])

            diff=diff + abs(neuronValues[i+1,j]-neuronValues[i,j]) 

    diff=diff/(2*8*9)
    
    return diff    
    
    
def main():
    
    parent = MatrixCreate(10,50)
    parent = MatrixRandomize(parent)
    fitness = VectorCreate(5000)
    ##call fitness1 for a thru c and 2 for d thru f
    parentFitness = Fitness2(parent)
    neuronValues = MatrixCreate(10,10)
    for i in range(10):
        neuronValues[0,i] = 0.5
    for i in range(9):
        Update(neuronValues,parent,i)
    
    

    for currentGeneration in range(1000):
        fitness[currentGeneration] = parentFitness
        
        child = MatrixPerturb(parent, 0.05)
        childFitness = Fitness2(child)
        
        if childFitness > parentFitness:
            parent = child
            parentFitness = childFitness
    
    for i in range(9):
        Update(neuronValues,parent,i)
    matplotlib.pyplot.imshow(neuronValues, cmap=matplotlib.pyplot.cm.gray, aspect='auto', interpolation='nearest')
##    plt.plot(fitness)
##            
##    
##    plt.axis([0,1000,0,.9])
    
    plt.show()
 
main()
