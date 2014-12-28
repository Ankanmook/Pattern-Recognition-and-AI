import sys
import math
from decimal import *

# Object representing individual symbols in a math expression.
# Contains a truth value, stroke information, and feature functions.
class Symbol:
    def __init__(self, truth):
        self.truth = truth
        self.classifiedAs = ''
        self.strokes = []
        self.minTraceDataRef = sys.maxint
        self.featureVector = []
    def addStroke(self, stroke, traceDataRef):
        self.strokes.append(stroke)
        if(int(traceDataRef) < int(self.minTraceDataRef)):
            self.minTraceDataRef = traceDataRef

    def printSymbol(self):
        print "Symbol: ", self.truth
        print "Number of Strokes: ", len(self.strokes)
