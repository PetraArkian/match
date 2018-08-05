class Match():

    def __init__(self, bigList, littleList):
        self._bigs = bigList
        self._littles = littleList

    @property
    def littles(self):
        return self._littles

    def makeMatches(self):
        for b in self._bigs:
            b.rank()

        for l in self._littles:
            l.rank()

        allPaired = False
        while(not allPaired):
            for l in self._littles:
                l.propose()

            for b in self._bigs:
                b.acceptProposal()

            allPaired = True
            print("allPaired == true")
            for l in self._littles:
                if(not l.isPaired):
                    print("allPaired == false")
                    allPaired = False
        print("everyone paired up")

    def displayResults(self):
        for l in self._littles:
            l.printPair()
