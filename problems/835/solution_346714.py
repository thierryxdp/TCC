def melhor_volta(matriz):
    minimo=min(matriz[0])
    crrdr=1
    for i in matriz:
        if min(i)<=minimo:
            minimo=min(i)
            crrdr=matriz.index(i)+1
    return crrdr,minimo,matriz[crrdr-1].index(minimo)+1