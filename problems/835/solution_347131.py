def melhor_volta(matriz):
    listacorridas = []
    for corredor in matriz:
        menortempo = min(corredor)
        listacorridas.append(menortempo)
    indice = listacorridas.index(min(listacorridas))
    volta = matriz[indice].index(min(listacorridas))
    return (indice+1,listacorridas[indice],volta)