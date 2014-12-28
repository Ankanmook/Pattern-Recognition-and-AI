# Simple container for expressions (collections of symbols)
class Expression():
    def __init__(self, filename):
        self.symbols = []
        self.filename = filename
    def addSymbol(self, symbol):
        self.symbols.append(symbol)

    def printExpression(self):
        print "Expression: "
        print self.filename
        print "Number of Symbols: ", len(self.symbols)
        for symbol in self.symbols:
            symbol.printSymbol()
