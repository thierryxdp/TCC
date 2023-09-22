def melhor_volta(matriz):
    menorTempo=0
    menor=0
    listaAux=[]
    for corredores in matriz:
        menorTempo=min(corredores)
        listaAux.append(menorTempo)
    menor=min(listaAux)
    return menor