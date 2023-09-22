def media_matriz(matriz):
    lista1=[]
    n_elementos=0
    soma=0
    for L in range(len(matriz)):
        for C in range(len(matriz[L])):
            soma+=matriz[L][C]
            n_elementos = n_elementos + 1
    return round(soma/n_elementos,2)