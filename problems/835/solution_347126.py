def melhor_volta(matriz):
    listacorridas = [[]]
    for corredor in matriz:
        menortempo = min(corredor)
        listacorridas.append(menortempo)
    indice = listacorridas.index(min(listacorridas))
    print(listacorridas)
    print(indice)
    for corrida in matriz[indice]:
        if corrida == min(listacorridas):
            volta = volta + 0
        else:
            volta = volta + 1
    print(volta)
    return (indice,listacorridas[indice],volta+1)