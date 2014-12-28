import math
from decimal import *
 

# ADD FEATURE FUNCTIONS HERE
'''
[1] Number of strokes,
[2] Number of Loops,
[3] Number of cusps,
[4] Number of Intersection,
[5] Initial and End Position direction,
[6] Point distribution [9 feature]
[6] Width to height ratio(Aspect Ratio)

'''
def normalizeExp(exp):
    symbols = exp.symbols

    minx = 99999.0
    maxx = -99999.0
    miny = 99999.0
    maxy = -99999.0

    for sym in symbols:
        strokes = sym.strokes
        for stroke in strokes:
            for (x,y) in stroke:
                x = float(x)
                y = float(y)
                if(x > maxx):
                    maxx = x
                if(x < minx):
                    minx = x

                if(y > maxy):
                    maxy = y
                if(y < miny):
                    miny = y

    rangex = float((maxx - minx))
    rangey = float((maxy - miny))

    for sym in symbols:
        strokes = sym.strokes
        newStrokes = []
        for stroke in strokes:
            newStroke = []
            for (x,y) in stroke:
                x = float(x)
                y = float(y)
                newx = (x - minx) / rangex
                newy = (y - miny) / rangey

                newStroke.append((newx, newy))
            newStrokes.append(newStroke)
        sym.strokes = newStrokes



def findAngle(xcurrent,ycurrent,xprevious,yprevious,xpenultimate,ypenultimate):

    ab = math.pow(xprevious - xcurrent,2) + math.pow(yprevious - ycurrent,2)
    ab = math.sqrt(ab)
    bc = math.pow(xpenultimate - xprevious,2) + math.pow(ypenultimate - yprevious,2 )
    bc = math.sqrt(bc)
    ac = math.pow(xcurrent - xpenultimate,2) + math.pow(ycurrent - ypenultimate,2 )
    ac = math.sqrt(ac)

    if (ab == 0 or bc == 0) :
        return float(math.pi/2)
    else :
        angleb = (math.pow(ab,2) + math.pow(bc,2) - math.pow(ac,2) ) / (2 * ab * bc) 
        if(angleb >= 1 ) :
            return 2 * math.pi
        if(angleb <= -1 ) :
            return math.pi

    return math.acos(angleb)



def findAreaof(edges):

    # total number of edges
    n = len(edges) 
    area = 0.0

    for i in range(n):
        j = (i + 1) % n
        area += float(edges[i][0]) * float(edges[j][1])
        area -= float(edges[j][0]) * float(edges[i][1])
    area = abs(area) / 2.0
    return area


def numberOfCusps(strokes):

    cusps = 0
    # Angle thresholds up to 170 degree
    angleT = 2.96705973         
    radians = 0.00
    totalpoints = 0

    # Counts the number of elements in a stroke
    # and calculates the total length of individual stroke
    for stroke in strokes:

        n = 0

        xprevious = 0.00
        xcurrent = 0.00
        yprevious = 0.00
        ycurrent = 0.00
        xpenultimate = 0.00
        ypenultimate = 0.00

        # One individual stroke at a time
        # Aspect Ratio and the cusps
        for coordinate in stroke:
            n += 1

            xcurrent = float(coordinate[0])
            ycurrent = float(coordinate[1])             

            xpenultimate = xprevious
            ypenultimate = yprevious
            xprevious = xcurrent
            yprevious = ycurrent


            radians = findAngle(xcurrent,ycurrent,xprevious,yprevious,xpenultimate,ypenultimate)
            if(radians < angleT):
                cusps += 1

        totalpoints = totalpoints + n

    return float(cusps)




def numberofIntersection(strokes): 

    '''
    Intra-Stroke Intersection
    and
    Inter-Stroke Intersection
    '''

    intersectionCount = 0

    xprevious = 0.00
    xcurrent = 0.00
    yprevious = 0.00
    ycurrent = 0.00
    n = 0

    len = 0.00
    angleTMax = 6.10865238 # 350 degree
    angleTMin = 0.174532925

    lineSegments = []

    for stroke in strokes:
        for coordinate in stroke:

            n += 1

            xcurrent = float(coordinate[0])
            ycurrent = float(coordinate[1])

            if ( xprevious == xcurrent):
                slope = 'infinity'
            else :
                slope =  float (yprevious - ycurrent) / float (xprevious - xcurrent)

            xprevious = xcurrent
            yprevious = ycurrent

            lineSegments.append( (xcurrent,ycurrent,xprevious,yprevious,slope) )


    for line1 in lineSegments :
        for line2 in lineSegments :
            slope1 = line1[4]
            slope2 = line2[4]

            x1 = line1[0]
            y1 = line1[1]
            x2 = line1[2]
            y2 = line1[3]
            x3 = line2[0]
            y3 = line2[1]
            x4 = line2[2]
            y4 = line2[3]

            if (slope1 != slope2):
                # intersection possible
                # sum of 4 angles should be equal to 350 degree threshold or less than 10 degree
                alpha = findAngle(x1,y1,x3,y3,x2,y3)
                beta = findAngle(x3,y3,x2,y2,x4,y4)
                gamma = findAngle(x2,y2,x4,y4,x1,y1)
                delta = findAngle(x4,y4,x1,y1,x2,y2)

                sumangle = alpha + beta + gamma + delta

                if (sumangle > angleTMax ):
                    intersectionCount += 1

    return intersectionCount

    # Aspect Ratio 
def aspectRatio(strokes):
    if(len(strokes) == 1 and len(strokes[0]) == 1):
        return (1.0, float(strokes[0][0][0]), float(strokes[0][0][0]), float(strokes[0][0][1]), float(strokes[0][0][1]))

    xMinimum = 0.00
    yMinimum = 0.00
    xMaximum = 0.00
    yMaximum = 0.00
    xcurrent = 0.00
    ycurrent = 0.00

    # Counts the number of elements in a stroke
    # and calculates the total length of individual stroke
    for stroke in strokes:

        #Aspect Ratio 
        for coordinate in stroke:

            # find maximum and minimum coordinate in x and y vectors
            if (xcurrent > xMaximum):
                xMaximum = xcurrent
            if (ycurrent > yMaximum):
                yMaximum = ycurrent
            if (xcurrent < xMinimum):
                xMinimum = xcurrent
            if (ycurrent < yMinimum):
                yMinimum = ycurrent

            xcurrent = float(coordinate[0])
            ycurrent = float(coordinate[1])       

    try:
        aspectRatio = math.fabs( (xMaximum - xMinimum) / (yMaximum - yMinimum))
    except: 
        aspectRatio = 0

    return (aspectRatio,xMaximum,xMinimum,yMaximum,yMinimum)




def pointDistribution(strokes):

    totalElement = 0.00

    lst = aspectRatio(strokes)
    aspect   = lst[0]
    xMaximum = lst[1]
    xMinimum = lst[2]
    yMaximum = lst[3]
    yMinimum = lst[4]

    distribution1 = 0.00
    distribution2 = 0.00
    distribution3 = 0.00
    distribution4 = 0.00
    distribution5 = 0.00
    distribution6 = 0.00
    distribution7 = 0.00
    distribution8 = 0.00
    distribution9 = 0.00

    x0 = xMinimum
    x1 = xMinimum + float(xMaximum  - xMinimum)/3
    x2 = xMinimum + 2 * float(xMaximum  - xMinimum)/3
    x3 = xMaximum

    y0 = yMinimum
    y1 = yMinimum + float(yMaximum  - yMinimum)/3
    y2 = yMinimum + 2 * float(yMaximum  - yMinimum)/3
    y3 = yMaximum
    '''
    Block 11
    '''
    xmin11 = x0 
    xmax11 = x1
    ymin11 = y0
    ymax11 = y1

    '''
    Block 12
    '''
    xmin12 = x1 
    xmax12 = x2
    ymin12 = y0
    ymax12 = y1

    '''
    Block 13
    '''
    xmin13 = x2 
    xmax13 = x3
    ymin13 = y0
    ymax13 = y1

    '''
    Block 21
    '''
    xmin21 = x0 
    xmax21 = x1
    ymin21 = y1
    ymax21 = y2


    '''
    Block 22
    '''
    xmin22 = x1
    xmax22 = x2
    ymin22 = y1
    ymax22 = y2

    '''
    Block 23
    '''
    xmin23 = x2
    xmax23 = x3
    ymin23 = y1
    ymax23 = y2


    '''
    Block 31
    '''
    xmin31 = x0 
    xmax31 = x1
    ymin31 = y2
    ymax31 = y3


    '''
    Block 32
    '''
    xmin32 = x1
    xmax32 = x2
    ymin32 = y2
    ymax32 = y3

    '''
    Block 33
    '''
    xmin33 = x2
    xmax33 = x3
    ymin33 = y2
    ymax33 = y3

    for stroke in strokes :
        for coordinate in stroke:

            totalElement += 1.00

            x = float(coordinate[0])
            y = float(coordinate[1])

            #For block 11
            if( x >= xmin11) and (x < xmax11) and (y >= ymin11) and (y < ymax11) :
                distribution1 += 1

            #For block 12
            if( x >= xmin12) and (x < xmax12) and (y >= ymin12) and (y < ymax12) :
                distribution2 += 1

            #For block 13
            if( x >= xmin13) and (x < xmax13) and (y >= ymin13) and (y < ymax13) :
                distribution3 += 1

            #For block 21
            if( x >= xmin21) and (x < xmax21) and (y >= ymin21) and (y < ymax21) :
                distribution4 += 1

            #For block 22
            if( x >= xmin22) and (x < xmax22) and (y >= ymin22) and (y < ymax22) :
                distribution5 += 1

            #For block 23
            if( x >= xmin23) and (x < xmax23) and (y >= ymin23) and (y < ymax23) :
                distribution6 += 1

            #For block 31
            if( x >= xmin31) and (x < xmax31) and (y > ymin31) and (y <= ymax31) :
                distribution7 += 1

            #For block 32
            if( x > xmin32) and (x < xmax32) and (y > ymin32) and (y <= ymax32) :
                distribution8 += 1

            #For block 33
            if( x > xmin33) and (x <= xmax33) and (y > ymin33) and (y <= ymax33) :
                distribution9 += 1


    distribution1 = float(distribution1)/ float (totalElement)
    distribution2 = float(distribution2)/ float (totalElement)
    distribution3 = float(distribution3)/ float (totalElement)
    distribution4 = float(distribution4)/ float (totalElement)
    distribution5 = float(distribution5)/ float (totalElement)
    distribution6 = float(distribution6)/ float (totalElement)
    distribution7 = float(distribution7)/ float (totalElement)
    distribution8 = float(distribution8)/ float (totalElement)
    distribution9 = float(distribution9)/ float (totalElement)

    return (aspect,distribution1,distribution2,distribution3,distribution4,distribution5,distribution6,distribution7,distribution8,distribution9)


def initialEndPosition(strokes):

    orientation = -1
    angle = 0.00
    slope = 0.00

    xinitial = float(strokes[0][0][0])
    yinitial = float(strokes[0][0][1])

    for stroke in strokes :
        for coordinate in stroke:
            xfinal = float(coordinate[0])
            yfinal = float(coordinate[1])


    if(xfinal == xinitial) :
        if(yfinal - yinitial) > 0 :
            angle = math.pi/2
        else :
            if(yfinal - yinitial) < 0 :
                angle = 3 * math.pi/2
            else :
                if (yfinal == yinitial):
                    angle = 0.00
                else :
                    angle = -1.00

    else :
        slope = float(yfinal - yinitial) / (xfinal - xinitial)
        if(slope < 0):
            # Second Quadrant
            if( (yfinal - yinitial) > 0   and (xfinal - xinitial) < 0 ) : 
                angle = math.atan(slope) + math.pi/2
            else :
                # Fourth Quadrant
                if( (yfinal - yinitial) < 0   and (xfinal - xinitial) > 0 ) :
                    angle = math.atan(slope) + 3 * math.pi/2
        else :
            # Third quadrant
            if ((yfinal - yinitial) <0) and ( (xfinal - xinitial) < 0):
                angle = math.atan(slope) + math.pi
            else:
                # First Quadrant
                angle = math.atan(slope)


    '''
    Following direction and their discrete values
    North (0) , 
    East(1), ,West(2)
    South (5)     
    '''

    # East
    if (angle >= (7 * math.pi/4) or angle < math.pi /4 ) :
        orientation = 1

    #North
    if ( (angle >=  (math.pi /4)) and (angle <  (3 * math.pi/4 ))  ):
        orientation = 0 

    # west
    if ( (angle >=  (3 * math.pi /4)) and (angle < (5 * math.pi/4)) ):
        orientation = 2

    # South
    if ( (angle >=  (5 * math.pi /4))  and (angle < (7 * math.pi/4)) ):
        orientation = 3

    return orientation

def getFeatureVector(strokes):
    stroke = len(strokes)
    #loop = self.numberofloops()
    distribution = pointDistribution(strokes)
    cusps = numberOfCusps(strokes)
    intersections = numberofIntersection(strokes)
    iep = initialEndPosition(strokes)

   # print "Symbol: ", self.truth
   # print "Number of Strokes: ", str(stroke)      
   # print "Number of Loops:", str(loop)
   # print "Aspect Ratio", str(distribution[0]) 
   # print "Distribution", str(distribution[1]),str(distribution[2]),str(distribution[3]),str(distribution[4]),str(distribution[5]),str(distribution[6]),str(distribution[7]),str(distribution[8]),str(distribution[9])
   # print "Number of Cusps", str(cusps)
   # print "Intersections", str(intersections)
   # print "InitialEndPosition", str(initialEndPosition)


    '''
    Returns loops,cusps,intersection,Initial End Position ,aspectRatio)distribution[0],distributions
    '''
    return [stroke,cusps,intersections,iep,distribution[0],distribution[1],distribution[2],distribution[3],distribution[4],distribution[5],distribution[6],distribution[7],distribution[8],distribution[9]]  
