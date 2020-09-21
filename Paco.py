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
    print(transitionArray)
    print(alphabetArray)
    print(statesArray)
    
    return transitionArray

leerArchivo("prueba.txt")
