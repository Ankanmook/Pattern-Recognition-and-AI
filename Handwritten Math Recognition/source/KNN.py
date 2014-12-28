from pylab import *
from Symbol import *
from Exp import *

class KNN():
    def __init__(self, trainingSet, minFv, maxFv):
        # Append training folds to create training set.
        self.features = trainingSet

    # Calculate the n-dimensional euclidean distance between
    # two vectors.
    def edist(self, xs, ys):
        sum = 0
        for x,y in zip(xs, ys):
            sum += (x - y) ** 2
            
        return (sum ** 0.5)

    def classify(self, target):
        best_dist = 999999999
        best_class = ''
        for f in self.features:
            dst = self.edist(target, f[0])
            if(dst < best_dist):
                best_dist = dst
                best_class = f[1]
        return best_class
