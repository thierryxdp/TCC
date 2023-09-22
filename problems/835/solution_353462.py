def melhor_volta(matriz):
    minimo=999999999999999
    for x in matriz:
        if min(x)<minimo:
            minimo=min(x)
            posicao=list.index(x,minimo)
            volta=list.index(matriz,x)
    return (posicao+1,minimo, volta+1)