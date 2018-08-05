"""
Bigs
"""


#from datetime import datetime
import queue

class Big(object):

    #initialization
    def __init__(self, name, bday, data):
        self._name = name
        self._bday = bday
        self._littleList = None
        self._paired = False
        self._pair = None
        self._proposals = queue.Queue()
        self._littleRankings = {}
        self._data = data

    @property
    def name(self):
        return self._name

    @property
    def isPaired(self):
        return self._paired

    @property
    def bday(self):
        return self._bday

    def getData(self):
        return self._data

    def setLittles(self, littleList):
        self._littleList = littleList

    def rank(self):
        for l in self._littleList:  # looking at one big
            index = 0  # used to iterate through data sets
            i = 0  # factored into big rank
            multiplier = 1  # factored into weighted big rank
            for item in self._data[
                index]:  # each element in 'data' is a list. this line is looking at one of those lists
                if type(item) is int:  # this list corresponds to a rank weight
                    multiplier = item  # the final rank sum will be multiplied by this weight
                    index = index + 1  # moves onto next element in data
                if item in l.getData()[index]:  # sums the number of items in each element list in common
                    i = i + 1
            # print(i)
            self._littleRankings[l] = i * multiplier

    def recieveProposal(self, l):
        self._proposals.put(l)


    def acceptProposal(self):
        if(self._pair == None) & (not self._proposals.empty()):
            self._pair = self._proposals.get()
            self._paired = True
        while(not self._proposals.empty()):
            suitor = self._proposals.get()
            if(self._littleRankings[self._pair] > self._littleRankings[suitor]):
                self._pair.getRejected()
                self._pair = suitor
            else:
                suitor.getRejected()

    def display(self):
        print(self._name + " " + self._bday)




