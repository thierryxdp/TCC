def conta_numero(numero,matriz):
    """conta e retorna quantas vezes o numero de entrada aparece na matriz.
    int,list->int"""
    n=0
    for i in range(len(matriz)):
        for j in matriz[i][j]:
            if numero==j:
                n=n+1
    return n