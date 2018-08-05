from Big import Big
from Little import Little
from match import Match



def read(file_path):
    i = 0
    with open(file_path, "r") as f:
        f.readline()
        # skip top row (Timestamp,Full Name,Birthday,Favorite Color,How important is this too you?,
        # Which shows do you like)
        output = [[],[]]
        for line in f:
            line = line.split('\t')  # split with 'tab'
            line = line[1:]  # remove timestamp
            if i%2 == 0:
                line.insert(0, "Big")
            else:
                line.insert(0, "Little")
            # shows = line[-1].rstrip('\n').split(';') # list of tv shows
            data = []
            for s in line:
                s = s.rstrip('\n')
                s = s.split(',')
                data.append(s)
            # data.append(shows)
            if (data[0][0] == 'Big'):
                print("Big")
                name = data[1][0]
                bday = data[2][0]
                data.reverse()
                output[0].append(Big(name, bday, data))
                i += 1
            elif (data[0][0] == 'Little'):
                print("Little")
                name = data[1][0]
                bday = data[2][0]
                data.reverse()
                output[1].append(Little(name, bday, data))
                i += 1
        print("Number of participants: " + str(i))
        return output


if __name__ == "__main__":
    output = read("/Users/codywan/Desktop/match/Match-Test-Responses-Form-Responses-1.tsv")
    print("running")
    bigList = output[0]
    littleList = output[1]

    for b in bigList:
        b.setLittles(littleList)

    for l in littleList:
        l.setBigs(bigList)

    matchMaker = Match(output[0],output[1])
    matchMaker.makeMatches()
    print("made matches")
    matchMaker.displayResults()

    with open("pairs.txt", "w") as f:
        for little in matchMaker.littles:
            f.writelines("{0} {1}, {2}\n".format(little.name, little.bday, little.pair.name))
            f.writelines("{0} {1}, {2}\n".format(little.pair.name, little.pair.bday, little.name))
