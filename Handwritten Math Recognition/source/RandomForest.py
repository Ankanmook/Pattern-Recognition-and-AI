from Symbol import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC

class RandomForest():
    def __init__(self, trainingset):
        self.features = trainingset
        self.train()

    def train(self):
        forest = RandomForestClassifier(n_estimators=50, criterion='entropy', max_depth=10)
        #forest = SVC()
        X = []
        Y = []
        print "Reformatting feature vectors..."
        for f in self.features:
            X += [f[0]]
            Y += [f[1]]
        print 
        print "Done."

        lastlen = len(X[0])
        for x in X:
            if(lastlen != len(x)):
                print "BAD: "
                print x

        print "Fitting..."
        forest.fit(X,Y)
        self.forest = forest

    def classify(self, X):
        return self.forest.predict(X)

