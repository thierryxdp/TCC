def melhor_volta(matriz):
    menorTempo=0
    menor=0
    listaAux=[]
    indice=0
    corredor=0
    i=0
    for corredores in matriz:
        menorTempo=min(corredores)
        listaAux.append(menorTempo)
    menor=min(listaAux)
    while i < len(matriz):
        if menor in matriz[i]:
            indice=list.index(matriz[i],menor)
            corredor=i
    return (menor, indice, corredor)