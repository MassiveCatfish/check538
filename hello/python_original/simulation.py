import math
import random
import json
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np



# White/Black refer to the white/black dots, poll/kitchen refer to poll only/poll plus

def adddata(pollWhite, pollBlack, kitchenWhite, kitchenBlack, dataname):
    i=0
    totallen = len(dataname["model"])
    # only want the larger sets
    while (i < totallen and (len(dataname["model"][i])>4)):
        curCandidate = dataname["model"][i]["candidate_name"]
        curState = dataname["model"][i]["state"]
        curPoll = dataname["model"][i]["pollonly_winprob"]
        curKitchen = dataname["model"][i]["kitchen_winprob"]
        curWeight = 1 #change later for other metrics
        if (Winners[curState][0]==curCandidate) or (Winners[curState][1]==curCandidate):
            pollWhite.append(curPoll)
            kitchenWhite.append(curKitchen)
        else:
            pollBlack.append(curPoll)
            kitchenBlack.append(curKitchen)
        i += 1

def windowAverage(numPoints, windowSize, lstWhite, lstBlack):
    returnlst = []
    for i in range(1, numPoints):
        midpoint = 100*float(i)/numPoints
        lower = midpoint - windowSize*0.5
        upper = midpoint + windowSize*0.5
        whiteCount = len([x for x in lstWhite if (x> lower and x < upper)])
        blackCount = len([x for x in lstBlack if (x> lower and x < upper)])
        std = binomialStd(float(midpoint)/100, whiteCount+blackCount)
        returnlst.append((midpoint,ratioWhite(whiteCount,blackCount),std, whiteCount,blackCount))
    return returnlst


def tupleIntoLst(listoftuples):
    xlst = []
    ylst = []
    zlst = []
    for x in listoftuples:
        xlst.append(x[0])
        ylst.append(x[1])
        zlst.append(x[2])
    return (xlst,ylst,zlst)


def ratioWhite(numW, numB):
    if numW==0 and numB==0:
        return float("inf")
    else:
        return float(numW)/float(numW+numB)*100


def binomialStd(p, N):
    if p==0 or N==0:
        return 0
    else:
        return 100*(math.sqrt(N*p*(1-p)))/N


def logchoose(n, r):
    return math.log(math.factorial(n))-math.log(math.factorial(r))-math.log(math.factorial(n-r))




#p: head prob, x: needed to win, n: total available
def headWinProb(p, x, n):
    totalprob = float(0)
    if x > n:
        return 0
    elif x<0:
        return float(100)
    for i in range(x,n+1):
        curprob = logchoose(n,i)+ i*math.log(p) + (n-i)*math.log(1-p)
        totalprob += math.exp(curprob)
    return float(100)*totalprob

#pairwise subtract
def listSubtract (listA, listB):
    listC = []
    for i in range(len(listA)):
        listC.append(listA[i]-listB[i])
    return listC

#pairwise add
def listAdd (listA, listB):
    listC = []
    for i in range(len(listA)):
        listC.append(listA[i]+listB[i])
    return listC




def simulateCoin(HwinWhite, HwinBlack, numTrials, numCoins):
    lstOfTrials = []
    for i in range(numTrials):
        totalH = 0
        totalT = 0
        curHadvLst = [] #current Head advantage
        curHwinLst = []
        for j in range(numCoins):
            if random.randint(0,1):
                totalH += 1
            else:
                totalT += 1
            curHadvantage = totalH - totalT
            curHadvLst.append(curHadvantage)
            curHeadWinProb = headWinProb(0.5, (numCoins+1)/2-totalH, numCoins-totalH-totalT)
            curHwinLst.append(curHeadWinProb)
        if totalH > totalT:
            HwinWhite.extend(curHwinLst)
        else:
            HwinBlack.extend(curHwinLst)
        lstOfTrials.append((curHadvLst,curHwinLst))
    return lstOfTrials



def main():
    HwinWhite = []
    HwinBlack = []
    simResult = simulateCoin(HwinWhite, HwinBlack, 20, 201)
    print "HwinWhite len: "+str(len(HwinWhite))
    print "HwinBlack len: "+str(len(HwinBlack))
    HwinFinal = windowAverage(50,4,HwinWhite, HwinBlack)
    print "Coin toss - Heads win:"
    print HwinFinal
    (xHwin,yHwin,sig) = tupleIntoLst(HwinFinal)
    print "Heads win prob:"
    #plt.plot(xHwin,xHwin)
    yxdiff = listSubtract(yHwin,xHwin)
    plt.plot(xHwin,listSubtract(xHwin,xHwin), 'k-', label="zero")
    plt.plot(xHwin,yxdiff, 'b-', label="Oracle")
    #plt.plot(xHwin,listSubtract(yxdiff,sig), 'g-', label="Oracle-upper")
    #plt.plot(xHwin,listAdd(yxdiff,sig), 'g-', label="Oracle-lower")
    plt.show()


    

def main2():
    HwinWhite = []
    HwinBlack = []
    trialLength = 201
    numberOfTrials = 21
    simResult = simulateCoin(HwinWhite, HwinBlack, numberOfTrials, trialLength)
    print "HwinWhite len: "+str(len(HwinWhite))
    print "HwinBlack len: "+str(len(HwinBlack))
    HwinFinal = windowAverage(200,1,HwinWhite, HwinBlack)
    (xHwin,yHwin,sig) = tupleIntoLst(HwinFinal)
    steps = range(1,trialLength+1)
    zeros = np.zeros(trialLength)
    ones = np.ones(trialLength)*50
    print steps
    for i in range(1,21):
        plt.figure(i)
        plt.subplot(211)
        # i = number of trails
        # head advantage graph
        plt.plot(steps,simResult[i][0],'b-', steps, zeros, 'k-')
        plt.plot

        plt.subplot(212)
        # winning probability
        plt.plot(steps,simResult[i][1],'b-',steps, ones, 'k-')
        plt.show()


if __name__ == "__main__":
    main2()
