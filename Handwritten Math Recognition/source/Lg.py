import sys
from Symbol import *
from Exp import *

def sortSymbols(e):
    symbols = e.symbols
    newList = []
    traceDataRef = -1
    while(len(newList) != len(symbols)):
        currentMin = sys.maxint
        minIndex = -1
        for i in range(len(symbols)):
            s = symbols[i]
            if(int(s.minTraceDataRef) > int(traceDataRef)):
                if(int(s.minTraceDataRef) < int(currentMin)):
                    currentMin = int(s.minTraceDataRef)
                    minIndex = i

        traceDataRef = currentMin
        newList.append(symbols[minIndex])
    return newList

# Create a string correpsonding to the true label graph of the given expression.
def ExpToLgTruth(e):
    symbols = sortSymbols(e)
    filename = e.filename

    lg = '#Nodes\n\n'
    # Print nodes
    n = 0
    for s in symbols:
        truth = s.truth

        strokes = s.strokes
        for stroke in strokes:
            lg += 'N, ' + str(n) + ', ' + str(truth) + ", 1.0\n"
            n += 1

    lg += '\n\n#Edges\n\n'

    # Print edges
    n = 0
    for i in range(len(symbols)):
        s1 = symbols[i]
        stks1 = s1.strokes
        for j in range(len(stks1)):
            ns = n + j
            n2 = ns + 1
            
            # Mark edge for previous strokes in symbol
            for k in range(0, j):
                lg += "E, " + str(ns) + ", " + str(n + k) + ", *, 1.0\n"

            # Do remaining strokes for this symbol.
            for k in range(j+1, len(stks1)):
                lg += "E, " + str(ns) + ", " + str(n2) + ", *, 1.0\n"
                n2 += 1

            # Do rest of symbols.
            for k in range(i+1, len(symbols)):
                s2 = symbols[k]
                stks2 = s2.strokes
                for stk in stks2:
                    lg += "E, " + str(ns) + ", " + str(n2) + ", R, 1.0\n"
                    n2 += 1
        n += len(stks1)

    return lg

# Create a string correpsonding to the segmented and classified label 
# graph of the given expression.
def ExpToLgSegmented(e):
    symbols = e.segSymbols
    filename = e.filename

    lg = '#Nodes\n\n'
    # Print nodes
    n = 0
    for s in symbols:
        truth = s.classifiedAs

        strokes = s.strokes
        for stroke in strokes:
            lg += 'N, ' + str(n) + ', ' + str(truth) + ", 1.0\n"
            n += 1

    lg += '\n\n#Edges\n\n'

    # Print edges
    n = 0
    for i in range(len(symbols)):
        s1 = symbols[i]
        stks1 = s1.strokes
        for j in range(len(stks1)):
            ns = n + j
            n2 = ns + 1
            
            # Mark edge for previous strokes in symbol
            for k in range(0, j):
                lg += "E, " + str(ns) + ", " + str(n + k) + ", *, 1.0\n"

            # Do remaining strokes for this symbol.
            for k in range(j+1, len(stks1)):
                lg += "E, " + str(ns) + ", " + str(n2) + ", *, 1.0\n"
                n2 += 1

            # Do rest of symbols.
            for k in range(i+1, len(symbols)):
                s2 = symbols[k]
                stks2 = s2.strokes
                for stk in stks2:
                    lg += "E, " + str(ns) + ", " + str(n2) + ", R, 1.0\n"
                    n2 += 1
        n += len(stks1)

    return lg
