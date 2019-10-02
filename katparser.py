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
    print("Number of problems: " + str(allproblems))
    print("Number of problems solved: " + str(solvedproblems))
    print("You have solved: " + ratiostring + "% of all problems")


def parse():
    #TODO find the latest datafile and call parse with that file as argument
    print("I AM PARSING!")


def parse(filename):
    print("I AM PARSING A SPECIFIC FILE")
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
            difficulty.append(result[8])
            solved.append(result[9])
        findnumofproblems()