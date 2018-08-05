"""
Littles
"""

import queue


class Little(object):
    # initialization
    def __init__(self, name, bday, data):
        self._name = name
        self._bday = bday
        self._paired = False
        self._pair = None
        self._bigQueue = queue.Queue()
        self._bigList = None
        self._data = data
        self._bigRankings = {}

    @property
    def name(self):
        return self._name

    @property
    def isPaired(self):
        return self._paired

    @property
    def pair(self):
        return self._pair

    @property
    def bday(self):
        return self._bday

    def getData(self):
        return self._data

    def setBigs(self,bigList):
        self._bigList = bigList

    def rank(self):
        for b in self._bigList: #looking at one big
            index = 0 #used to iterate through data sets
            i = 0 #factored into big rank
            multiplier = 1 #factored into weighted big rank
            for item in self._data[index]: #each element in 'data' is a list. this line is looking at one of those lists
                if type(item) is int:      #this list corresponds to a rank weight
                    multiplier = item;     #the final rank sum will be multiplied by this weight
                    index = index + 1      #moves onto next element in data
                if item in b.getData()[index]: #sums the number of items in each element list in common
                    i = i + 1
            # print(i)
            self._bigRankings[b] = i * multiplier #if there was a weight, i will be multiplied accordingly

        self._bigList = reversed(sorted(self._bigRankings, key=self._bigRankings.__getitem__)) #in the hash table, more desirable bigs have a higher value (later in a list).
                                                                                               #we want to use a queue, so we sort the bigList by the hash table, then reverse it
                                                                                               #so the most desirable big is first in the queue

        for b in self._bigList:
            self._bigQueue.put(b) #put the list into a queue

    def propose(self):
        if(not self._paired):
            self._pair = self._bigQueue.get()
            self._paired = True
            self._pair.recieveProposal(self)

    def getRejected(self):
        self.display()
        print("got rejected")
        self._pair = None
        self._paired = False

    def printPair(self):
        print()
        self.display()
        print("matched with")
        self._pair.display()


    def display(self):
        print(self._name + " " + self._bday)

