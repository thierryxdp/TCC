def melhor_volta(matriz):
    menorTempo=0
    listaAux=[]
    for corredores in matriz:
        menorTempo=min(corredores)
        listaAux.append(menorTempo)
    return listaAux