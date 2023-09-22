def melhor_volta(matriz):
    '''retorna uma tupla indicando a melhor de quem foi a melhor volta e com qual tempo
    [6][10] -> tuple'''
    bestRun = -1
	for i in list(range(1,7)):
        minTempo = min(matriz[i-1])
        mtIndex = matriz[i-1].index(minTempo)
        if(minTempo < bestRun or bestRun == -1):
            bestTuple = (i, matriz[i-1][mtIndex], mtIndex)
            
    return bestTuple