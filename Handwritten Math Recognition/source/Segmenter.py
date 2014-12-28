from Exp import Expression
from Symbol import *
from Features import *

class Segmenter():
    def __init__(self):
        pass




    # Segment the given expression and calculate the features.
    def segment(self, exp):
        setattr(exp, "strokes", [])
        setattr(exp, "segSymbols", [])
    
        for s in exp.symbols:
            for stroke in s.strokes:
                exp.strokes.append(stroke)

        strokeNo = 0

        for stroke in exp.strokes:
            s = Symbol('?')
            s.addStroke(stroke, strokeNo)
            s.featureVector = getFeatureVector(s.strokes)
            #s.featureVector = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            strokeNo += 1
            exp.segSymbols.append(s)

