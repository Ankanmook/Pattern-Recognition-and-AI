from Exp import *
from Symbol import *
from Lg import *
from Features import *

import sys
import pickle
import xml.etree.ElementTree as ET
import os

# Filenames in expressions contain both path information and 
# the filename (with no extension). Create the directory if needed.
def createDirs(filename):
    segments = filename.split('/')
    result = ''
    for i in range(len(segments) - 1):
        result += segments[i] + '/'

    if not os.path.exists(result):
        os.makedirs(result)

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


if(len(sys.argv) != 2):
    print "Usage: python FinalClassifier.py <filename>"
    sys.exit()

# Determine filename for expression (sans directory prefix)
filename = sys.argv[1]
exp = readExpression(filename)
splt = filename.split('/')
splt2 = splt[len(splt) - 1].split('.')
exp.filename = splt2[0]

# Load classifiers.
print "Loading classifiers..."
forest = pickle.load(open("FOREST.p"))
knn = pickle.load(open("KNN.p"))
classMap = pickle.load(open("classmap.p"))
print "Finished loading classifiers."

# Make sure the LG directories exist.
createDirs("./results/truth/")
createDirs("./results/forest/")
createDirs("./results/knn/")

# Write the truth label graph
lgTruth = ExpToLg(exp, useTruth=True)
f = open("results/truth/" + exp.filename + ".lg", 'wb')
f.write(lgTruth)

forestlg = ''
knnlg = ''

# Forest classifier
for s in exp.symbols:
    fv = getFeatureVector(s.strokes)

    classifiedAs = classMap[forest.classify(fv)[0]]
    s.classifiedAs = classifiedAs

lgForest = ExpToLg(exp)
f = open("results/forest/" + exp.filename + ".lg", 'wb')
f.write(lgForest)

# 1NN classifier
for s in exp.symbols:
    fv = getFeatureVector(s.strokes)

    classifiedAs = classMap[knn.classify(fv)]
    s.classifiedAs = classifiedAs

lgKNN = ExpToLg(exp)
f = open("results/knn/" + exp.filename + ".lg", 'wb')
f.write(lgKNN)
