# A01376544 Mariana Caballero
# A01377744 Alejandro Torices
# A01745530 Pablo García
# A01374561 Paco Murillo


from itertools import combinations


def createDict(finishedTransitionArray, statesArray, alphabetArray):
    for index in range(len(statesArray)):
        finishedTransitionArray.append([])
        list = finishedTransitionArray[index]
        for index in range(len(alphabetArray)):
            list.append([])


def leerArchivo(dirTxtFile):
    file = open(dirTxtFile, 'r', encoding='UTF-8')
    transitionArray = file.read().split('),(')
    transitionArray[0] = transitionArray[0][2::]
    transitionArray[len(transitionArray)-1] = transitionArray[len(transitionArray)-1][:len(transitionArray[len(transitionArray)-1])-2:]
    alphabetArray = []
    alphabetAndStateFlag = False
    statesArray = []
    for index in range(len(transitionArray)):
        transitionArray[index] = transitionArray[index].split(',')
        for indexIn in range(len(transitionArray[index])):
            if indexIn == 0:
                workingArray = alphabetArray
            else:
                workingArray = statesArray

            for string in workingArray:
                if string == transitionArray[index][indexIn]:
                    alphabetAndStateFlag = True
                    break
            if alphabetAndStateFlag:
                alphabetAndStateFlag = False
            else:
                workingArray.append(transitionArray[index][indexIn])

    finishedTransitionArray = []
    createDict(finishedTransitionArray, statesArray, alphabetArray)

    for list in transitionArray:
        stateIndex = statesArray.index(list[1])
        letterIndex = alphabetArray.index(list[0])
        finishedTransitionArray[stateIndex][letterIndex].append(list[2])
    
    return finishedTransitionArray, alphabetArray, statesArray


def createPowersetStates(statesArray):
    DFAStates = []
    for index in range(len(statesArray)+1):
        for comb in combinations(statesArray, index):
            stateName = ""
            for string in comb:
                stateName += string
            DFAStates.append(stateName)

    return DFAStates


def createTransitions(DFAStates, statesArray, alphabetArray, transitionArray):
    DFATransitions = []
    createDict(DFATransitions, DFAStates, alphabetArray)
    for indexAlpha in range(len(alphabetArray)):
        for indexStates in range(len(DFAStates)):
            workingList = DFATransitions[indexStates][indexAlpha]
            for letterState in DFAStates[indexStates]:
                for outState in transitionArray[statesArray.index(letterState)][indexAlpha]:
                    try:
                        if workingList[0].find(outState) == -1:
                            workingList[0] += outState
                    except IndexError:
                        workingList.append(outState)

    return DFATransitions


def createTxt(DFAStates, DFATransitions, alphabetArray):
    outString = "{"

    for indexState in range(len(DFAStates)):
        for indexAlpha in range(len(alphabetArray)):
            try:
                outString += "("+alphabetArray[indexAlpha]+","+DFAStates[indexState]+","+DFATransitions[indexState][indexAlpha][0]+"),"
            except IndexError:
                if indexState != 0:
                    outString += "(" + alphabetArray[indexAlpha] + "," + DFAStates[indexState] + ",∅),"
                else:
                    outString += "(∅,∅,∅),"
                    break
    outString = outString[:len(outString)-1:]+"}"

    file = open("DFA.txt", 'w', encoding='UTF-8')
    file.write(outString)
    file.close()



def main():
    transitionArray, alphabetArray, statesArray = leerArchivo(input("Nombre del archivo: "))
    print(alphabetArray)
    print(statesArray)
    print(transitionArray)
    DFAStates = createPowersetStates(statesArray)
    print(DFAStates)
    DFATransitions = createTransitions(DFAStates, statesArray, alphabetArray, transitionArray)
    print(DFATransitions)
    createTxt(DFAStates, DFATransitions, alphabetArray)


    # {(1,p,p),(0,p,q),(0,q,r),(1,q,r),(0,r,s),(1,r,p),(0,s,s),(1,s,s)}
    # 1*0E0E*


main()
