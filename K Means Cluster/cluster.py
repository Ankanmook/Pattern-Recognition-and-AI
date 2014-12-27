# cluster.py
#
# K Means Algorithm
# K = 2: K = 5; K = 10
#
# Version 1.0
# Author: Ankan Mookherjee, September 6, 2013

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import random
import sys


'''
Generates K means cluster for input matrxi and K value and iterations
'''
def KMeans(input,K,iteration):

    x_matrix = []
    y_matrix = []
    
    clusterMatrix = []
    
    xmax = 0.00
    xmin = 0.00
    xmax = 0.00
    ymin = 0.00
    
    for row in input:
        new_row = []   
        x_matrix.append(float64(row[0]))
        y_matrix.append(float64(row[1]))
        new_row.append( float64(row[0]))
        new_row.append( float64(row[1]))
        clusterMatrix.append(new_row)
    
               
    clusterMatrix = np.array(clusterMatrix)
    
    x_matrix = np.array(x_matrix)
    y_matrix = np.array(y_matrix)

    xmax = x_matrix.max()
    xmin = x_matrix.min()
    ymax = y_matrix.max()
    ymin = y_matrix.min()
    
    
    #beta = np.dot(clusterMatrix.T,clusterMatrix)
    
    '''
    #print clusterMatrix
    print beta
    print xmax
    print xmin
    print ymax
    print ymin
    '''
    
    means = generateRandomMean(K,xmax,xmin,ymax,ymin)
    
    cluster(means,clusterMatrix,K,iteration)
    
    return 0

'''
Clustering for the first time
'''
def cluster(means,clusterMatrix,K,iteration):
    
    euclideanx = 0.00
    euclideany = 0.00
    distance = 0.00
    
    distancematrix = []
    
    for row in clusterMatrix:
        d = []
        for i in range(0,K):
            euclideanx = means[i][0] - row[0]
            euclideany = means[i][1] - row[1]
            distance = math.pow(euclideanx,2) + math.pow(euclideany,2)
            distance = math.pow(distance, 0.5)
            d.append(distance)
        distancematrix.append(d)
        
    distancematrix = np.array(distancematrix)
    
    classvalue = []
    matrixWithClass = []
    
    # Find ClassValue
    for row in distancematrix:
        dmin = row.min()
        classv = []
        for i in range(0,K):
            if (dmin == row[i]):
                classv.append(i)
        classvalue.append(classv)
        
    classvalue = np.array(classvalue)
    
    index = 0
    
    for row in clusterMatrix: 
        new_row = []
        new_row.append(row[0])
        new_row.append(row[1])
        new_row.append(classvalue[index][0])
        matrixWithClass.append(new_row)
        
        index = index + 1

    
    matrixWithClass = np.array(matrixWithClass)
    
    #print distancematrix
    #print classvalue
    #print matrixWithClass
    calculateMean(matrixWithClass,K,means,iteration)
    
    
    return 0;

'''
Calculate new-mean from given input matrix
and old mean 
'''
def calculateMean(matrixWithClass,K,oldmeans,iteration):
    
    totalitem = []
    
    for i in range(0,K):
            totalitem.append(0)
            
    totalitem = np.array(totalitem)
    
    means = []
    
    for i in range(0,K):
        averageItemX = []
        averageItemY = []
        mean = []
        for row in matrixWithClass:
            if (row[2] == i):
                averageItemX.append(row[0])
                averageItemY.append(row[1])
        xmean = np.mean(averageItemX)
        ymean = np.mean(averageItemY)
        mean.append(xmean)
        mean.append(ymean)
        means.append(mean)
    
    means = np.array(means)
    
    #print totalitem
    #print means
    
    converge(matrixWithClass,oldmeans,means,K,iteration)
    return 0


'''
Converging. Trying till 20 iterations
'''
def converge(matrixWithClass,oldmeans,newmeans,K,iteration):
   
    '''    
    Total iteration I am considering is 20
    ''' 
    if(iteration == 20):
        
        print 'Old Mean :' + str(oldmeans)
        print 'Current Mean :'+ str(newmeans)
        print 'Iteration :' + str(iteration)
        
        plotKMeans(matrixWithClass,K,newmeans)
    
    else:
        iteration = iteration + 1
        print 'Old Mean :' + str(oldmeans)
        print 'Current Mean :'+ str(newmeans)
        print 'Iteration :' + str(iteration)
        cluster(newmeans,matrixWithClass,K,iteration)
        
    
    
    return 0

'''
Plotting K means algorithm
'''
def plotKMeans(matrixWithClass,K,means):
            
    nwcolor = []
    nwcolor.append('red')
    nwcolor.append('green')
    nwcolor.append('orange') #1
    nwcolor.append('cyan')
    nwcolor.append('brown')
    nwcolor.append('yellow')
    nwcolor.append('magenta')
    nwcolor.append('purple')
    nwcolor.append('lightgreen')
    nwcolor.append('blue')
    
    index = 1
    '''
    Plotting of graph
    '''
    plot_Matrix = []
    
    decision_boundary_x = []
    decision_boundary_y = []

    xaxis = -3.0
    yaxis = -3.0
 
    for i in range(0,K):
        averageItemX = []
        averageItemY = []
        mean = []
        for row in matrixWithClass:
            if (row[2] == i):
                averageItemX.append(row[0])
                averageItemY.append(row[1])
        plt.scatter(averageItemX,averageItemY,marker='*',color = nwcolor[i]) 
    
    '''
    Plotting decision boundary
    '''
    
    
    while yaxis < 3.0:
        xaxis = -3.0
        while xaxis < 5.0:
            newrow = []
            newrow.append(xaxis)
            newrow.append(yaxis)
            plot_Matrix.append(newrow)
            
            xaxis = xaxis + 0.1
        
        yaxis = yaxis + 0.1
    
    plot_Matrix = np.array(plot_Matrix)
    
    
    

    while index < 4401 :
        
        d = []
        for i in range(0,K):
            euclideanx = means[i][0] - plot_Matrix[index-1][0]
            euclideany = means[i][1] - plot_Matrix[index-1][1]
            distance = math.pow(euclideanx,2) + math.pow(euclideany,2)
            distance = math.pow(distance, 0.5)
            d.append(distance)
        
        d = np.array(d)
        dmin = d.min()
        # Find ClassValue
        for i in range(0,K):
            if (dmin == d[i]):
                oldclassvalue = i
                     
        d = []
        for i in range(0,K):
            euclideanx = means[i][0] - plot_Matrix[index][0]
            euclideany = means[i][1] - plot_Matrix[index][1]
            distance = math.pow(euclideanx,2) + math.pow(euclideany,2)
            distance = math.pow(distance, 0.5)
            d.append(distance)
            
        d = np.array(d)
        dmin = d.min()    
        # Find ClassValue
        for i in range(0,K):
            if (dmin == d[i]):
                newclassvalue = i
        
        
        if (oldclassvalue != newclassvalue):
            new_x_boundary = (plot_Matrix[index-1][0] + plot_Matrix[index][0])/2
            new_y_boundary = (plot_Matrix[index-1][1] + plot_Matrix[index][1])/2 
            decision_boundary_x.append(new_x_boundary)
            decision_boundary_y.append(new_y_boundary)
        index = index + 2

    
    plt.scatter(decision_boundary_x,decision_boundary_y,marker='.',color = 'black',label = 'Decision boundary')
    plt.axis([-4,6,-3,4])
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    
    ttl = str(K)+ ' K Means'
    plt.title(ttl)
    
    plt.show()



def generateRandomMean(K,xmax,xmin,ymax,ymin):
    
    means = []
    
    for i in range(0,K):
        mean = []
        mean.append(random.uniform(xmax,xmin))
        mean.append(random.uniform(ymax,ymin))
        means.append(mean)
    
    means = np.array(means)
    
    #print means
    
    return means


'''
Main Function
'''
def main():
    
    # Create column (or array)
    input = np.random.random(size=(1000,1000))

    # Save to file
    np.savez('data.npy',input)

    # Read from file    
    input = np.load('data.npy')
    
    '''
    Cluster K-Means for K =2/5/10
    '''
    strK = raw_input("Enter the desired K:")

    KMeans(input,2,float(strK))
    
    
main()


