import random
import math
import pickle
import copy
from datetime import datetime
import time
from Symbol import *
from Exp import *
from Lg import *

import pylab as PL
import xml.etree.ElementTree as ET

        
# Read a single expression from the given file.
def readExpression(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    strokes = {}

    # Collect all of the traces (strokes)
    for trace in root.iter():
        if(trace.tag == "{http://www.w3.org/2003/InkML}trace"):
            traceid = trace.attrib['id']
            tracetext = trace.text.strip().split(',')
        
            tracecoords = []
            for t in tracetext:
                coords = t.strip().split(' ')
                tracecoords.append( (coords[0],coords[1]) )
        
            # Save the stroke
            strokes[traceid] = tracecoords

    # Go through each traceGroup and put together symbol objects.

    tgroot = root.find("{http://www.w3.org/2003/InkML}traceGroup")
    rawfilename = filename.split('.')[0]
    newexpression = Expression(rawfilename)

    first = True
    for tg in tgroot.iter():
        if(tg.tag == "{http://www.w3.org/2003/InkML}traceGroup"):
            truth = tg.find("{http://www.w3.org/2003/InkML}annotation").text
            if(first):
                # traceGroup for entire segmentation
                first = False
                continue

            newsymbol = Symbol(truth)

            for elem in tg.iter():
                if(elem.tag == "{http://www.w3.org/2003/InkML}traceView"):
                    tvindex = elem.attrib['traceDataRef']
                    newsymbol.addStroke(strokes[tvindex], tvindex)
            newexpression.addSymbol(newsymbol)
    return newexpression

# Read in all of the expressions from the given filelist.
def readAllExpressions(filelist):
    print "Reading in expressions..."
    numExpressions = 0
    with open(filelist) as f:
        numExpressions = len(list(f))

    f = open(filelist, 'r')    
    progress = 0
    expressions = []
    t = time.time()
    for line in f:
        filename = 'data/' + line.strip()
        print progress, " / ", numExpressions, " - ", filename,
        try:
            exp = readExpression(filename)
        except:
            print "Failed reading ", filename
        #exp.printExpression()
        #print "--------------"
        expressions.append(exp)
        progress += 1
        t2 = time.time()
        print t2 - t
        t = t2

    return expressions


def getClasses(P):
    classes = {}
    for exp in P:
        symbols = exp.symbols
        for s in symbols:
            classes[s.truth] = 1

    return classes.keys()

def getProbability(P, c):
    numSamples = 0
    i = 0

    for exp in P:
        symbols = exp.symbols
        numSamples += len(symbols)

        for s in symbols:
            if(s.truth == c):
                i += 1

    return float(i) / float(numSamples)

def klDivergenceScore(P, Qs):
    classes = getClasses(P)
    score = 0

    for Q in Qs:
        for j in classes:
            pP = getProbability(P, j)
            pQ = getProbability(Q, j)
            
            if(pQ != 0):
                score += math.log(pP / pQ) * pP
    return score

def createFolds(e, numIterations):
    exps = copy.deepcopy(e)

    random.shuffle(exps)
    length = len(exps)
    f1 = []
    for i in range(length/3):
        f1.append(exps.pop())

    f2 = []
    for i in range(length/3):
        f2.append(exps.pop())

    f3 = []
    while(len(exps) > 0):
        f3.append(exps.pop())

    folds = [f1, f2, f3]

    oldKLScore = klDivergenceScore(e, folds)
    for i in range(numIterations):
        if(i % 100 == 0):
            print "Iteration ", i, " at ", datetime.now()

        # Choose which folds to swap from.
        fswap1 = random.randint(0, 2)
        fswap2 = fswap1
        while(fswap1 == fswap2):
            fswap2 = random.randint(0, 2)

        f1i = random.randint(0, len(folds[fswap1])-1)
        f2i = random.randint(0, len(folds[fswap2])-1)

        temp = folds[fswap1][f1i]
        folds[fswap1][f1i] = folds[fswap2][f2i]
        folds[fswap2][f2i] = temp

        newKLScore = klDivergenceScore(e, folds)

        # If the new divergence is lower, keep it, otherwise swap back.
        if(oldKLScore < newKLScore):
            temp = folds[fswap1][f1i]
            folds[fswap1][f1i] = folds[fswap2][f2i]
            folds[fswap2][f2i] = temp
        else:
            oldKLScore = newKLScore

    return [f1, f2, f3]

def plotHist(exp):
    classes = getClasses(exp)
    numClasses = len(classes)
    classMap = {}
    for i in range(numClasses):
        c = classes[i]
        classMap[c] = i

    distExp = []

    for e in exp:
        symbols = e.symbols
        for s in symbols:
                i = classMap[s.truth]
                distExp.append(i)

    PL.hist(distExp, numClasses)
    

# ====================== #

def createAndSaveFolds(filelist, plot=False):
    print "READING IN EXPRESSIONS"
    exps = readAllExpressions(filelist)
    classes = getClasses(exps)
    numIterations = 1000

    print "CREATING FOLDS..."
    folds = createFolds(exps, numIterations)
    if(plot):
        plotHist(folds[0])
        PL.figure()
        plotHist(folds[1])
        PL.figure()
        plotHist(folds[2])

    pickle.dump(folds, open("folds.p", "wb"))
    print "FINISHED FOLDS AT ", datetime.now()

    foldtest = pickle.load(open("folds.p", "rb"))
    foldtest[1][20].printExpression()
    ExpToLg(foldtest[1][20])
    print "SUCCESSFULLY LOADED FOLD"

def loadFolds():
    print "Loading folds..."
    (f1,f2,f3) = pickle.load(open("fold1_final.p"))
    print "Successfully loaded folds."

    return (f1, f2, f3)

createfolds = True

if(createfolds):
    filelist = 'AllEM_part4_TRAIN_all.txt'

    exps = readAllExpressions(filelist)
    plotHist(exps)
    PL.figure()

    createAndSaveFolds(filelist, plot=True)
    PL.show()



