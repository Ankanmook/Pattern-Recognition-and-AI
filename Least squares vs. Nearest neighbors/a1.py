# a1.py
#
# Generate Nearest Neighbor and Least Square Classifier for .npy data file,
# For Assignment 1
#
# Version 1.0
# Author: Ankan Mookherjee, September 6, 2013

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import sys


'''
Generates Least Square Classifier Function to plot the Least Square Classifier
Function Parameters : Takes input Matrix which has all varaibles
Function Returns : None
'''
def classifyLeastSquare(input):

    numberofrow = 0
    numberofcolumn = 0
    
    xelementnumber = 0
    yelementnumber = 0
    
    for row in input :
        if len(row) == 0:
            continue
        for element in row:
            numberofcolumn = numberofcolumn + 1
        numberofrow = numberofrow + 1 

    
    
    X = np.random.rand(numberofrow, 2)
    Y = np.random.rand(numberofrow, 1)
    beta = np.random.rand(numberofrow,1)

    X.fill(0.00000);
    Y.fill(1.00000);
    
    # Fill Matrix X and Matrix Y
    for row in input:
        if len(row) == 0:
            continue
        for element in row:
            if (float(element) != float64(0.0)) and (float(element) != float64(1.0)) :
                X.itemset(xelementnumber,float64(element))
                xelementnumber = xelementnumber + 1
            if float(element) == 0.0 or float(element) == 1.0 :
                Y.itemset(yelementnumber,float64(element))
                yelementnumber = yelementnumber + 1
    
    # B^ = (XT X)-1XT y    
    beta = np.dot(X.T,X)
    beta = np.linalg.inv(beta)
    beta = np.dot(beta,X.T)
    beta = np.dot(beta,Y)
    
    plotLeastSquare(beta,input)
    
    
    return 0


'''
Plot Least Square Classifier Function to plot the Least Square Classifier
Function Parameters : Takes beta Matrix
Function Returns : None
'''
def plotLeastSquare(beta,inputMatrix):
        
    x0 = -4.0
    y0 = beta[1]+beta[0]*x0   
    
    xend = 6.0
    yend = beta[1]+beta[0]*xend
    
    linelistx = []
    linelisty = []
    
    linelistx.append(x0)
    linelistx.append(xend)
    
    linelisty.append(y0)
    linelisty.append(yend)
    
    list0forx = []
    list0fory = []
    list1forx = []
    list1fory = [] 
    
    # Scatter Plotting the points in Lines
    for row in inputMatrix:
        if float64(row[2]) == float64(0.0) :
            list0forx.append(row[0])
            list0fory.append(row[1])
        else :
            list1forx.append(row[0])
            list1fory.append(row[1])
    
    plt.scatter(list0forx,list0fory,marker='.',color = 'orange',label = '0 Elements') 
    plt.scatter(list1forx,list1fory,marker='.',color ='c',label = '1 Elements')
    plt.plot(linelistx,linelisty,color='black', linewidth=1.0,label = 'Classification Boundary')
    plt.axis([-4,6,-3,4])
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Least Square Plot')
    
    plt.show()
    # Saving the figure as pdf file
    #plt.savefig('LeastSquare.pdf')
    
       
    
    
    profit0 = 0    
    profit1 = 0
    loss0 = 0
    loss1 = 0
    
    
    # Create Confusion Matrix
    for row in inputMatrix:
        yhat = beta[1]+beta[0]*row[0]
        
        if float64(yhat - row[1])> float64(0.0) and float64(row[2]) == float64(0.0) :
            profit0 = profit0 + 1
        if float64(yhat - row[1])> float64(0.0) and float64(row[2]) == float64(1.0) :
            loss1 = loss1 + 1
        if float64(yhat - row[1])< float64(0.0) and float64(row[2]) == float64(0.0) :
            loss0 = loss0 + 1
        if float64(yhat - row[1])< float64(0.0) and float64(row[2]) == float64(1.0) :
            profit1 = profit1 + 1
    
    print 'Confusion Matrix for Least Square : '
    print ' '
    print ''+ '   0' + '|' + ' 1 '
    print '0 '+str(profit0) + '|' + str(loss0)
    print '1 '+str(loss1)+ '|' + str(profit1)

    
    group0Profit = float64(profit0/float64(profit0+loss0)*100)
    group1Profit = float64(profit1/float64(profit1+loss1)*100)
    TotalProfit = float64 ((profit0 + profit1)/float64(profit0 + profit1 + loss0 + loss1)*100)
        
    print
    print 'Correct Classification Rate for Least Square : '
    print ' '
    print 'For 0 Group : ' + str(group0Profit ) + '%'
    print 'For 1 Group : ' + str(group1Profit ) + '%'
    print 'Total Correct Classification :'+ str (TotalProfit ) + '%'
   
    return


# x axis -3 to 5
# y axis  -2.5 to 3

'''
Plot Nearest Neighbor Classifier for an Input Matrix with confusion matrix for Profit and Loss
Function Parameters : 
    Takes value of K - number of nearest neighbor comparison
    Takes input Matrix
Function Returns : None
'''
def classifyNearestConfusionMatrix(K,inputMatrix):
    
    profit0 = 0    
    profit1 = 0
    loss0 = 0
    loss1 = 0
    
    xaxis = -3
    yaxis = -2.5
    
    xdatapointsFor0 = []
    ydatapointsFor0 = []
    xdatapointsFor1 = []
    ydatapointsFor1 = []
    
    list0forx = []
    list0fory = []
    list1forx = []
    list1fory = []
    listforclassification = []
    decisionboundaryx = []
    decisionboundaryy = []
    
    previousxaxis = 0
    previousyaxis = 0
    previousClass = 0
    
    iter = 0  
    if (K == 1):
        valchange = 2
    
    else :
        valchange = 3
         
    while yaxis < 3:
        xaxis = -3
        while xaxis < 5:
            
            classifiedVal = classifyKnearest(K,inputMatrix,xaxis,yaxis)
            
            if classifiedVal == 0 :
                list0forx.append(xaxis)
                list0fory.append(yaxis)
                listforclassification.append(classifiedVal)
            
            if classifiedVal == 1 :
                list1forx.append(xaxis)
                list1fory.append(yaxis)
                listforclassification.append(classifiedVal)
            
            if (previousClass != classifiedVal) and (iter == valchange):
                decisionboundaryx.append((xaxis+previousxaxis)/2)
                decisionboundaryy.append((yaxis+previousyaxis)/2)
                                
            previousxaxis = xaxis
            previousyaxis = yaxis
            previousClass = classifiedVal
            
            if iter == valchange :
                iter = 0
            else :
                iter = iter + 1
            
            xaxis = xaxis + 0.1

        yaxis = yaxis + 0.1
    
    
    decisionboundaryx.append(3)
    decisionboundaryy.append(5)
    
    if(K == 1) or (K == 15):
        newdecisionboundaryx = sorted(decisionboundaryx)
        newdecisionboundaryy = sorted(decisionboundaryy)
        
        decisionboundaryx = []
        decisionboundaryy = []
        
        decisionboundaryx = newdecisionboundaryx
        decisionboundaryy = newdecisionboundaryy
        
    
    # Scatter Plotting the points in Lines
    for row in inputMatrix:
        if float64(row[2]) == float64(0.0) :
            xdatapointsFor0.append(row[0])
            ydatapointsFor0.append(row[1])
        else :
            xdatapointsFor1.append(row[0])
            ydatapointsFor1.append(row[1])
    
    # Plot for decision 
    plt.scatter(xdatapointsFor0,ydatapointsFor0,marker='.',color = 'orange',s=40, label = '0 Elements') 
    plt.scatter(xdatapointsFor1,ydatapointsFor1,marker='.',color ='b',s=40, label = '1 Elements')
    
    plt.scatter(list0forx,list0fory,marker='.',color = 'y',s=10,label = '0 Elements') 
    plt.scatter(list1forx,list1fory,marker='.',color ='c',s=10,label = '1 Elements')
    
    plt.plot(decisionboundaryx,decisionboundaryy,color='black', linewidth=0.5,label = 'Classification Boundary')
    
    plt.axis([-2.8,4,-2.5,3])
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    
    if K == 1 :
        plt.title('1 Nearest Neighbor Plot')
        #plt.savefig('1NN.pdf')
    else :
        plt.title('15 Nearest Neighbor Plot')
        #plt.savefig('15NN.pdf')
   
    plt.show()
    
        
    # Create Confusion Matrix
    for row in inputMatrix:
        classifiedVal = classifyKnearest(K,inputMatrix,row[0],row[1])
        if(classifiedVal == 0) and (row[2] == float64(0.0)):
            profit0 = profit0 + 1
        if(classifiedVal == 0) and (row[2] == float64(1.0)):
            loss0 = loss0 + 1
        if(classifiedVal == 1) and (row[2] == float64(1.0)):
            profit1 = profit1 + 1
        if(classifiedVal == 1) and (row[2] == float64(0.0)):
            loss1 = loss1 + 1
    
    if (K == 1) :        
        print 'Confusion Matrix for ' + str(K) + ' Nearest Neighbor : '
        print ' '
        print ''+ '   0 ' + '|' + '1 '
        print '0 '+str(profit0) + '|' + str(loss1)
        print '1 '+str(loss0)+ '  |' + str(profit1)

    if (K == 15) :
        print 'Confusion Matrix for ' + str(K) + ' Nearest Neighbor : '
        print ' '
        print ''+ '   0' + '|' + '1 '
        print '0 '+str(profit0) + '|' + str(loss1)
        print '1 '+str(loss0)+ '|' + str(profit1)
    
    
    group0Profit = float64(profit0/float64(profit0+loss1)*100)
    group1Profit = float64(profit1/float64(profit1+loss0)*100)
    TotalProfit = float64 ((profit0 + profit1)/float64(profit0 + profit1 + loss0 + loss1)*100)    
        
    print
    print 'Correct Classification Rate for ' + str(K) + 'NN : '
    print ' '
    print 'For 0 Group : ' + str(group0Profit ) + '%'
    print 'For 1 Group : ' + str(group1Profit ) + '%'
    print 'Total Correct Classification :'+ str (TotalProfit ) + '%'
    return 0




'''
This Function Classifies the points with K Nearest Neighbor Classification Algorithm
Function Parameters :
    Input K Value of K for nearest neighbor classification 1/15
    Input Matrix : one row of the matrix contains coordinates of point x,y and whether it is 0 or 1
    x,y coordinate needed to classify
Function Return :
    The point that is to be classified belongs to 0 or 1 group
'''
def classifyKnearest(K,inputMatrix,x,y):
    
    numberofrow = 0
    
    for row in inputMatrix :
        if len(row) == 0:
            continue
        numberofrow = numberofrow + 1 

    # One for x-coordinate,y-coordinate,classification, Euclidean Distance from given point
    DistanceMatrix = np.random.rand(numberofrow, 4)

    dictn = { }
    list = []
    sortedlist = []
    
    dictnGroup = {}
    
    for row in inputMatrix :
        # Calculating the Euclidean distance between the given point and all other points in data set
        xi = float64(row[0])
        yi = float64(row[1])
        d1 = (xi-x)*(xi-x)
        d2 = (yi-y)*(yi-y)
        d = math.sqrt(d1+d2)
        
        # Storing value in map object    
        dictn[d] = (row[0],row[1],float64(row[2]))
        
        #print dictnGroup
        #Storing distance in list object
        list.append(d)
        
    # Sort the list in ascending order
    sortedlist = sorted(list)

    # Sort the column based on the distance
    
    #Classifying the given point according to k Nearest Neighbor
    group0Count = 0
    group1Count = 0
    
    # The first index is the closest value which is the point distance itself
    for n in range(0,K) :
        val = dictn[sortedlist[n]]
        if ( float64(val[2]) == float64(0.0)) :
            group0Count = group0Count + 1
        #if (float64(val[2]) == float64(1.0)) :
        else :
            group1Count = group1Count + 1
    
    
    if (group0Count > group1Count ) :
        return 0
        # print 'New Point is in Group 0'
    else :
        return 1
        # print 'New Point is in Group 1'
       
    return 0



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
    
    print 'Please read the section of the Report in the Solution : How to interpret Confusion Matrix.'
    print 'Also look into the solution pdf to see the interpretation of the plot color'
    print 

    # Classify Least Square 
    classifyLeastSquare(input)
    
    # Classification for 1 N
    classifyNearestConfusionMatrix(1,input)
    
    # Classification for 15 N
    classifyNearestConfusionMatrix(15,input)
    
    
main()





