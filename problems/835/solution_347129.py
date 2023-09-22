def melhor_volta(matriz):
    listacorridas = []
    for corredor in matriz:
        menortempo = min(corredor)
        listacorridas.append(menortempo)
    indice = listacorridas.index(min(listacorridas))
    for corrida in matriz[indice]:
        if corrida == min(listacorridas):
            volta = volta + 0
        else:
            volta = volta + 1
    return (indice+1,listacorridas[indice+1],volta+1)