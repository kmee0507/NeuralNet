import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib

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
    for i in range(0,5):
        parent = MatrixCreate(1,50)
        parent = MatrixRandomize(parent)
        parentFitness = Fitness(parent)
        Genes = MatrixCreate(50,5000)
        fits = MatrixCreate(1,5000)

        for currentGeneration in range(5000):
            for j in range(50):
                Genes[j][currentGeneration] = parent[0][j]
            ##print currentGeneration, parentFitness
            child = MatrixPerturb(parent, 0.05)
            childFitness = Fitness(child)
            if childFitness > parentFitness:
                parent = child
                parentFitness = childFitness
            fits[0][currentGeneration] = parentFitness
            

        #PlotVectorAsLine(fits)
        
    print Genes
    plt.imshow(Genes, cmap = plt.cm.gray, aspect = 'auto', interpolation = 'nearest')
    plt.show()
main()
