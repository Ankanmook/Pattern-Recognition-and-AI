# a2map.py
#
# Generate MAP Classifier for .npy data file,
# For Assignment 2
#
# Version 1.0
# Author: Ankan Mookherjee, September 20, 2013

import random
import math
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from sys import argv, exit


'''
Classify the maximum value from arg-max
of Conditional probability function and return the
classified class
'''
def classify_argmax(Conditonal_Matrix):
    
    classification_Matrix = []
    
    for row in Conditonal_Matrix:
        if (row[0] > row [1] )  :
            classification_Matrix.append(0)
        else :
            if (row[1] > row [0] ) :
                classification_Matrix.append(1)
            
    classification_Matrix = np.array(classification_Matrix)
    
    return classification_Matrix

'''
Returns the conditional probablity into prior
probabilty matrix for a class of points
'''
def map_Classifier(Matrix_of_Class,prior_0,prior_1):
    
    map_Matrix = []

    for row in Matrix_of_Class:
        
        newrow = []
        
        map_0 = row[0]*prior_0 
        map_1 = row[1]*prior_1
        
        newrow.append(map_0)
        newrow.append(map_1)
        map_Matrix.append(newrow)
    
    map_Matrix = np.array(map_Matrix)
    
    return map_Matrix
    
    
'''
Function to calculate Mean
Returns an array of mean of the matrix
'''
def calculateMean(matrix):
    
    mean = []
    mean.append([0.0,0.0])
    
    rowcount = 0
    
    for row in matrix:
        rowcount = rowcount + 1
        mean[0][0] = float(row[0]) + float(mean[0][0])
        mean[0][1] = float(row[1]) + float(mean[0][1])
        
    mean[0][0] = mean[0][0]/rowcount
    mean[0][1] = mean[0][1]/rowcount
    
    return mean



'''
Calculates covariance matrix of a given matrix
'''
def covariance(Matrix,mean,rows):
    x_matrix = []
    y_matrix = []
    
    covariance_matrix = []
    
    for row in Matrix:
        newrow_X = []
        newrow_Y = []
        newrow_X.append(row[0] - mean[0][0])
        newrow_Y.append(row[1] - mean[0][1])
        x_matrix.append(newrow_X)
        y_matrix.append(newrow_Y)
    
    x_matrix = np.array(x_matrix)
    y_matrix = np.array(y_matrix)
    
    x_Transpose = x_matrix.T
    y_Transpose = y_matrix.T
    zeroth_index_matrix = np.dot(x_Transpose,x_matrix )
    first_index_matrix = np.dot(y_Transpose,x_matrix)
    second_index_matrix = np.dot(x_Transpose,y_matrix)
    third_index_matrix = np.dot(y_Transpose,y_matrix)
    
    newrow1 = []
    newrow2 = []
    
    newrow1.append(zeroth_index_matrix[0][0]/(rows-1))
    newrow1.append(first_index_matrix[0][0]/(rows-1))
    newrow2.append(second_index_matrix[0][0]/(rows-1))
    newrow2.append(third_index_matrix[0][0]/(rows-1))
    
    covariance_matrix.append(newrow1)
    covariance_matrix.append(newrow2)
    
    covariance_matrix = np.array(covariance_matrix)
    
    return covariance_matrix        
    
'''
Returns Conditional probability distribution
for class
'''
def exponent_function(x,y,mean,covariance):
        
    xval = x - mean[0][0] 
    yval = y - mean[0][1]
    
    matrix_X_mean = []
    
    matrix_X_mean.append(xval)
    matrix_X_mean.append(yval)
    matrix_X_mean = np.array(matrix_X_mean)
     
    matrix_X_mean_T = matrix_X_mean.T
    
    covariance_inverse = np.linalg.inv(covariance)
    final_matrix = np.dot(matrix_X_mean_T,covariance_inverse)
    final_matrix = np.dot(final_matrix,matrix_X_mean)
    
    exponent = -0.5 * (final_matrix)
    
    return exponent


'''
Returns condition probability mass function for a matrix of class
'''
def get_Conditional_Probablilty(Matrix_of_Class,matrix_0_mean,matrix_1_mean,covariance_0,covariance_1):
    
    conditional_probablity_Matrix = []
    
    for row in Matrix_of_Class:
        
        newrow = []
        '''
        Conditional Probability given class 0
        '''
        exponent = exponent_function(row[0],row[1],matrix_0_mean,covariance_0)
        det = np.linalg.det(covariance_0)
        normal = 1/ (2 * np.pi * (det ** (0.5) ))
        conditional_0 = normal * math.exp(exponent)
        
        '''
        Conditional Probability given class 1
        '''
        exponent = exponent_function(row[0],row[1],matrix_1_mean,covariance_1)
        det = np.linalg.det(covariance_1)
        normal = 1/ (2 * np.pi * (det ** (0.5) ))
        conditional_1 = normal * math.exp(exponent)
        
        newrow.append(conditional_0)
        newrow.append(conditional_1)
        
        conditional_probablity_Matrix.append(newrow)
        
    conditional_probablity_Matrix = np.array(conditional_probablity_Matrix)
    
    return conditional_probablity_Matrix

'''
Plots the MAP classifier using conditional probability function
and prior
'''
def plot(input_Matrix_0,input_Matrix_1,prior_0,prior_1,row_0,row_1):
    
    matrix_0_mean = calculateMean(input_Matrix_0)
    matrix_1_mean = calculateMean(input_Matrix_1)
    
    covariance_0 = covariance(input_Matrix_0,matrix_0_mean,row_0)
    covariance_1 = covariance(input_Matrix_1,matrix_1_mean,row_1)

    conditional_probablity_0 = get_Conditional_Probablilty(input_Matrix_0,matrix_0_mean,matrix_1_mean,covariance_0,covariance_1)
    conditional_probablity_1 = get_Conditional_Probablilty(input_Matrix_1,matrix_0_mean,matrix_1_mean,covariance_0,covariance_1)
    
    map_Matrix_0 = map_Classifier(conditional_probablity_0,prior_0,prior_1)
    map_Matrix_1 = map_Classifier(conditional_probablity_1,prior_0,prior_1)
    
    classfied_0 = classify_argmax(map_Matrix_0)
    
    classified_1 = classify_argmax(map_Matrix_1)
    
    one_as_one = 0
    one_as_zero = 0
    zero_as_zero = 0
    zero_as_one = 0
    
    zero_plot_x = []
    zero_plot_y = []
    
    one_plot_x = []
    one_plot_y = []
    
    index = 0
    for element in classfied_0:
        if float(element) == 0.0:
            zero_plot_x.append(input_Matrix_0[index][0])
            zero_plot_y.append(input_Matrix_0[index][1])
            zero_as_zero = zero_as_zero + 1
        if float(element) == 1.0:
            one_plot_x.append(input_Matrix_0[index][0])
            one_plot_y.append(input_Matrix_0[index][1])
            zero_as_one = zero_as_one + 1
        index = index + 1
        
    
    index = 0
    for element in classified_1:
        if float(element) == 0.0:
            zero_plot_x.append(input_Matrix_0[index][0])
            zero_plot_y.append(input_Matrix_0[index][1])
            one_as_zero = one_as_zero + 1
        if float(element) == 1.0:
            one_plot_x.append(input_Matrix_1[index][0])
            one_plot_y.append(input_Matrix_1[index][1])
            one_as_one = one_as_one + 1
        index = index + 1
    
    '''
    Plotting of graph
    '''
    plot_Matrix = []
    
    xaxis = -3.0
    yaxis = -3.0
    
    
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
    
    
    conditional_Probablilty_Matrix = []
    conditional_Probablilty_Matrix = get_Conditional_Probablilty(plot_Matrix,matrix_0_mean,matrix_1_mean,covariance_0,covariance_1)
    
    decision_boundary_x = []
    decision_boundary_y = []
    index = 1
    
    class_identification = []
    class_identification = classify_argmax(conditional_Probablilty_Matrix)
    
    index = 1
    
    while index < 4400 :
        oldclass = class_identification[index-1]
        newclass = class_identification[index]
        if (oldclass != newclass):
            new_x_boundary = (plot_Matrix[index-1][0] + plot_Matrix[index][0])/2
            new_y_boundary = (plot_Matrix[index-1][1] + plot_Matrix[index][1])/2 
            decision_boundary_x.append(new_x_boundary)
            decision_boundary_y.append(new_y_boundary)
        index = index + 1
    
    
    plt.scatter(zero_plot_x,zero_plot_y,marker='.',color = 'cyan',label = '0 Elements') 
    plt.scatter(one_plot_x,one_plot_y,marker='.',color = 'orange',label = '1 Elements') 
    plt.scatter(decision_boundary_x,decision_boundary_y,marker='.',color = 'black',label = 'Decision boundary')
    plt.axis([-3,5,-2.5,3])
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('MAP Classified Plot')
    plt.show()
        
    print 'Confusion Matrix: '
    print ' '
    print ''+ '   0' + '|' + '1 '
    print '0 '+str(zero_as_zero) + '|' + str(zero_as_one)
    print '1 '+str(one_as_zero)+ '|' + str(one_as_one)
    
    
    group0Profit = float (zero_as_zero / float(zero_as_zero + zero_as_one) * 100.0 ) 
    group1Profit = float (one_as_one / float(one_as_zero + one_as_one ) * 100.0 ) 
    TotalProfit = float((zero_as_zero + one_as_one ) / float(zero_as_zero + zero_as_one + one_as_zero + one_as_one) * 100.0 ) 
    
    print
    print 'Correct Classification Rate for MAP '
    print ' '
    print 'For 0 Group : ' + str(group0Profit ) + '%'
    print 'For 1 Group : ' + str(group1Profit ) + '%'
    print 'Total Correct Classification :'+ str (TotalProfit ) + '%'
    
    return 0


'''
Plots the normal user entered input matrix into
py plot
'''    
def plot_xy(input_Matrix_0,input_Matrix_1):
    
    zero_verctor_x = []
    zero_verctor_y = []
    
    one_verctor_x = []
    one_verctor_y = []
    
    for row in input_Matrix_0:
        zero_verctor_x.append(row[0])
        zero_verctor_y.append(row[1])
        
    
    for row in input_Matrix_1:
        one_verctor_x.append(row[0])
        one_verctor_y.append(row[1])
    
    
    plt.scatter(zero_verctor_x,zero_verctor_y,marker='.',color = 'cyan',s=40,label = '0 Elements')
    plt.scatter(one_verctor_x,one_verctor_y,marker='.',color = 'orange',s=40,label = '1 Elements')
    plt.axis([-3,5,-2.5,3])
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('The Given Plot')
    plt.show()
    
    return


'''
Main function
Program makes an entry here
'''    
def main():
    
    # Save to file
    #np.savez('data.npy',input)

    # Read from file    
    input = np.load('data.npy')
    
    input_Matrix_0 = []
    input_Matrix_1 = []
    
    row_0 = 0
    row_1 = 0
    
    for row in input:
        newrow_x = []
        newrow_y = []
        
        if float(row[2]) == 0.0 :
            newrow_x.append(row[0])
            newrow_x.append(row[1])
            input_Matrix_0.append(newrow_x)
            row_0 = row_0 + 1
        else :
            newrow_y.append(row[0])
            newrow_y.append(row[1])
            input_Matrix_1.append(newrow_y)
            row_1 = row_1 + 1
        
    input_Matrix_0 = np.array(input_Matrix_0)
    input_Matrix_1 = np.array(input_Matrix_1)

    prior_x = float(row_0 / row_0 + row_1)
    prior_y = float(row_1 / row_0 + row_1)
    
    plot_xy(input_Matrix_0,input_Matrix_1)
    plot(input_Matrix_0,input_Matrix_1,prior_x,prior_y,row_0,row_1)

    
main()