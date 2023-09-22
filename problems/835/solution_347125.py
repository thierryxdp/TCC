def melhor_volta(matriz):
    listacorridas = []
    for corredor in matriz:
        menortempo = min(corredor)
        listacorridas.append(menortempo)
    	indice = listacorridas.index(min(listacorridas))
    for corrida in matriz[indice]:
        qualvolta = 1
        if corrida != min(listacorridas):
            qualvolta += 1
    return (indice+1,listacorridas[indice],qualvolta)