import os

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
    print(str(solvedproblems) + " out of " + str(allproblems) + " problems solved\t\t" + progressbar(ratio) + " (" + ratiostring +"%)")


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
    print(solvedpointsstring+ " out of " + allpointsstring + " possible points\t" + progressbar(ratio) + " (" + ratiostring +"%)")


def findsolvedinranges():
    print(" ")
    print("Problems divided in difficulty:")
    for i in range(9):
        rank = i+1
        totalinrank = 0
        solvedinrank = 0
        # listofrankprobs = [j for j in difficulty if rank <= j < rank + 1]
        for j in range(len(problemnames)):
            if rank <= difficulty[j] < rank+1:
                totalinrank += 1
                if solved[j] == "solved\n":
                    solvedinrank +=1
        ratio = solvedinrank/totalinrank*100
        ratiostring = "%.2f" % ratio
        print("score " + str(rank) + "-" + str(rank+0.9) + ": solved " + str(solvedinrank) + "/" + str(totalinrank) + "\t\t" + progressbar(ratio) + " (" + ratiostring +"%)")


def findsolvedinallranges():
    print(" ")
    print("Problems divided in difficulty:")
    for i in range(100):
        rank = i
        totalinrank = 0
        solvedinrank = 0
        # listofrankprobs = [j for j in difficulty if rank <= j < rank + 1]
        for j in range(len(problemnames)):
            if rank == difficulty[j]*10:
                totalinrank += 1
                if solved[j] == "solved\n":
                    solvedinrank += 1
        if totalinrank > 0:
            ratio = solvedinrank / totalinrank * 100
            ratiostring = "%.2f" % ratio
            print("score " + str(rank/10) + ": solved " + str(solvedinrank) + "/" + str(totalinrank) + "\t\t" + progressbar(ratio) + " (" + ratiostring + "%)")


def progressbar(percent):
    WITDH = 20
    numofcharscompleted = int(percent/100*WITDH)
    barstring = "["
    for i in range(WITDH):
        if(i< numofcharscompleted):
            barstring += "■"
        else:
            barstring += " "
    barstring += "]"
    return barstring


def parse(filename = None, *args):
    if not filename:
        filename = "kattis-latest.txt"

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
            if "-" in result[8]:
                difficulty.append(0)
            else:
                difficulty.append(float(result[8]))
            solved.append(result[9])
    print(" ")
    findnumofproblems()
    findnumofpoints()
    findsolvedinranges()
    findsolvedinallranges()
