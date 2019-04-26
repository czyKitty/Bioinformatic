import sys

def readCommand(command):
    #Check flags
    if "-i" not in command:
        print("Missing -i arguement")
        sys.exit()
    if "-t" not in command:
        print("Missing -t arguement")
        sys.exit()
    if "-o" not in command:
        print("Missing -o arguement")
        sys.exit()
    #Check input
    if command.index("-i") < len(command)-1:
        inputFile = command[command.index("-i")+1]
        if inputFile[0] == "-":
            print("Missing input file name after -i")
            sys.exit()
    else:
        print("Missing input file name after -i")
        sys.exit()
    #Check threshold
    if command.index("-t") < len(command)-1:
        threshold = command[command.index("-t")+1]
        if threshold[0] == "-":
            print("Missing threshold after -t")
            sys.exit()
    else:
        print("Missing threshold after -t")
        sys.exit()
    #Check input
    if command.index("-o") < len(command)-1:
        outputFile = command[command.index("-o")+1]
        if outputFile[0] == "-":
            print("Missing output file name after -o")
            sys.exit()
    else:
        print("Missing output file name after -o")
        sys.exit()
    
    return [inputFile,threshold,outputFile] 


def uniqueGenes(fileText,threshold):
    uniqueGeneList = []
    line = fileText.readline()
    try:
        while line != "":
            if line.find("Query=") != -1:
                geneName = line.split(" ")[1]
                while line.find("Length=") == -1:
                    line = next(fileText)
                geneLen = int(line[line.find("=")+1:line.find("/n")])
                while line.find("Identities =") == -1 and line.find("No hits found") == -1:
                    line = next(fileText)
                if line.find("No hits found") != -1:
                    uniqueGeneList.append(geneName)
                else:
                    geneId = int(line[line.find("=")+2:line.find("/")])
                    if geneId/geneLen <= threshold:
                        uniqueGeneList.append(geneName)
            line = next(fileText)
    except StopIteration:
        return uniqueGeneList
    return uniqueGeneList
                        

def main():
    commandArgs = readCommand(sys.argv)
    inputFileName = commandArgs[0]
    threshold = commandArgs[1]
    outputFileName = commandArgs[2]
    fileText = open(inputFileName,'r')
    result = uniqueGenes(fileText,float(threshold))
    fileText.close()
    outputFile = open(outputFileName,'w')
    for gene in result:
        outputFile.write(gene+"\n")


    

main()
