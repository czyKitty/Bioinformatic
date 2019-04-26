import sys
import math

def dnaConserv(seqList):
    scoreList = []
    i = 0
    while i<len(seqList[0]):
        column = ""
        for item in seqList:
            column += item[i]
        countItem = ["A","C","G","T","-"]
        countTable = []
        for item in countItem:
            countTable.append(column.count(item))
        score = math.log(5,2)
        for item in countTable:
            if item != 0:
                score += item/len(seqList)*math.log(item/len(seqList),2)
        scoreList.append(score)
        i+=1
    return scoreList

def proteinConserv(seqList):
    scoreList = []
    i = 0
    while i<len(seqList[0]):
        column = ""
        for item in seqList:
            column += item[i]
        countItem = ["Y","W","V","T","S","R","Q","P","N","M","L","K","I","H","G","F","E","D","C","A","-"]
        countTable = []
        for item in countItem:
            countTable.append(column.count(item))
        score = math.log(5)
        for item in countTable:
            if item != 0:
                score += item/len(seqList)*math.log(item/len(seqList))
        scoreList.append(score)
        i+=1
    return scoreList

def readClustal(fileText):
    line = fileText.readline()
    seqNameList = []
    seqList = []
    try:
        while line != "":
            if line.find("CLUSTAL 2.1") != -1 or line.isspace() or line.find("*") != -1:
                line = next(fileText)
            else:
                if line.split()[0] not in seqNameList:
                    seqNameList.append(line.split()[0])
                    seqList.append(line.split()[1])
                else:
                    seqList[seqNameList.index(line.split()[0])] = seqList[seqNameList.index(line.split()[0])]+line.split()[1]
                line = next(fileText)
    except StopIteration:
        return seqList
    return seqList

def main():
    inputFileName = sys.argv[1]
    seqType = sys.argv[2]
    fileText = open(inputFileName,'r')
    if seqType == "DNA":
        result = dnaConserv(readClustal(fileText))
        outPut = open("conservationResult.txt",'w')
        for item in result:
            outPut.write(str(item)+"\n")
    elif seqType == "Protein":
        result = proteinConserv(readClustal(fileText))
        outPut = open("conservationResult.txt",'w')
        for item in result:
            outPut.write(str(item)+"\n")
    else:
        print("Invalid Type")

main()
