problemnames = []
subtotal = []
subaccept = []
subratio = []
fastesttime = []
usertotal = []
useraccept = []
userratop = []
difficulty = []
solved = []


def reset():
    problemnames.clear()
    subtotal.clear()
    subaccept.clear()
    subratio.clear()
    fastesttime.clear()
    usertotal.clear()
    useraccept.clear()
    userratop.clear()
    difficulty.clear()
    solved.clear()


def findnumofproblems():
    allproblems = len(problemnames)
    solvedproblems = solved.count("solved\n")
    ratio = solvedproblems/allproblems*100
    ratiostring = "%.2f" % ratio
    print(str(solvedproblems)+ " out of " + str(allproblems) + " problems solved (" + ratiostring +"%)")


def findnumofpoints():
    allpoints = sum(difficulty)+1
    allpointsstring = "%.1f" % allpoints
    solvedpoints = 1
    for i in range(len(solved)):
        if solved[i] == "solved\n":
            solvedpoints += difficulty[i]
    solvedpointsstring = "%.1f" % solvedpoints
    ratio = solvedpoints/allpoints*100
    ratiostring = "%.2f" % ratio
    print(solvedpointsstring+ " out of " + allpointsstring + " possible points(" + ratiostring +"%)")


def parse(filename = None):

    if filename is "":
        #TODO: fix seneste
        filename = "kattisdata-20191004223221.txt"
    reset()
    with open(filename, encoding="utf8") as fp:
        for line in fp:
            result = line.split("###")
            problemnames.append(result[0])
            subtotal.append(result[1])
            subaccept.append(result[2])
            subratio.append(result[3])
            fastesttime.append(result[4])
            usertotal.append(result[5])
            useraccept.append(result[6])
            userratop.append(result[7])
            difficulty.append(float(result[8]))
            solved.append(result[9])
        findnumofproblems()
        findnumofpoints()