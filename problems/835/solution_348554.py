def melhor_volta(matriz):
    i=0
    menor=0
    listaAux=[]
    indice=0
    corredor=0
    for corredores in matriz:
        listaAux.append(min(corredores))
    menor=min(listaAux)
    while i < len(matriz):
        if menor in matriz[i]:
            indice=list.index(matriz[i],menor)
            corredor=i
        i+=1
    return (corredor+1,menor, indice+1)