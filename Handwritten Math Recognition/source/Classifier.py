import pickle

from Symbol import *
from Exp import *
from RandomForest import *
from KNN import *
from Lg import *
from Features import *
from Segmenter import *

import pickle
import os

n_classes = 0

class Classifier():
    def __init__(self, quick=False):
        self.forest_correct = 0
        self.forest_total = 0
        self.initClassifier()

    def loadFolds(self):
        (f1,f2,f3) = pickle.load(open("folds.p"))

        print "Normalizing..."
        for exp in f1:
            normalizeExp(exp)
        for exp in f2:
            normalizeExp(exp)
        for exp in f3:
            normalizeExp(exp)
        print "Done."

        return (f1, f2, f3)

    # Convert folds (tuple of lists of expression objects)
    # to classifier-ready form - list of tuples (featurevector, truth)
    def foldsToTrainingSet(self, folds):
        trainingSet = []
        for exp in folds:
            symbols = exp.symbols
            for s in symbols:
                s.featureVector = getFeatureVector(s.strokes)
                #s.featureVector = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                trainingSet += [(s.featureVector, s.truth)]
        return trainingSet

    def segmentFold(self, fold):
        seg = Segmenter()
        for exp in fold:
            seg.segment(exp)
        return fold

    def initClassifier(self):
        print "Loading Folds..."
        folds = self.loadFolds()
        print "Done."

        print "Training Classifier..."
        # Config 1
        trainfolds = folds[0] + folds[1]
        testfold1 = folds[2]
        print "Calculating Features..."
        trainingSet = self.foldsToTrainingSet(trainfolds)
        print "Done."
        forest1 = RandomForest(trainingSet)
        print "First classifier complete."

        # Config 2
        trainfolds = folds[1] + folds[2]
        testfold2 = folds[0]
        trainingSet = self.foldsToTrainingSet(trainfolds)

        forest2 = RandomForest(trainingSet)
        print "Second classifier complete."

        # Config 3
        trainfolds = folds[2] + folds[0]
        testfold3 = folds[1]
        trainingSet = self.foldsToTrainingSet(trainfolds)

        forest3 = RandomForest(trainingSet)
        print "Third classifier complete."

        # Config 4 - All folds used
        trainfolds = folds[0] + folds[1] + folds[2]
        trainingSet = self.foldsToTrainingSet(trainfolds)

        forest4 = RandomForest(trainingSet)
        print "Final classifier complete."

        print "Segmenting Test Folds..."
        testfold1 = self.segmentFold(testfold1)
        testfold2 = self.segmentFold(testfold2)
        testfold3 = self.segmentFold(testfold3)
        print "Done."

        self.forests = [forest1, forest2, forest3, forest4]
        self.testsets = [testfold1, testfold2, testfold3]

    # Filenames in expressions contain both path information and 
    # the filename (with no extension). Create the directory if needed.
    def createDirs(self, filename):
        segments = filename.split('/')
        result = ''
        for i in range(len(segments) - 1):
            result += segments[i] + '/'

        if not os.path.exists(result):
            os.makedirs(result)

    # Use the specified classifier to classify the given expression.
    # Results will be written to an lg file, including the ground truth.
    def classify(self, i, exp):
        filename = 'lg/truth/' + exp.filename + '.lg'
        self.createDirs(filename)

        lg = ExpToLgTruth(exp)
        f = open(filename, 'w')
        f.write(lg)

        forest = self.forests[i]
        filename = 'lg/forest' + str(i+1) + '/' + exp.filename + '.lg'
        self.createDirs(filename)
        symbols = exp.segSymbols
        for s in symbols:
            if(len(s.featureVector) == 0):
                continue
            classifiedAs = forest.classify(s.featureVector)[0]
            if(classifiedAs == s.truth):
                self.forest_correct += 1
            else:
                print "Forest: ", s.truth, " classified as ", classifiedAs
            self.forest_total += 1
                
        lg = ExpToLgSegmented(exp)
        f = open(filename, 'w')
        f.write(lg)

c = Classifier()

for i in range(len(c.forests) - 1):
    print "\nRunning tests on set ", i+1
    n = 1
    total = len(c.testsets[i])
    for e in c.testsets[i]:
        c.classify(i, e)
        #print n
        n += 1
    print "Finished Set ", i
    print "Forest rate: ", c.forest_correct, " / ", c.forest_total
    print "\t= ", float(c.forest_correct)/float(c.forest_total)

    c.forest_correct = 0
    c.forest_total = 0
    c.knn_correct = 0
    c.knn_total = 0

