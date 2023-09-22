def conta_numero(numero,matriz):
    """conta e retorna quantas vezes o numero de entrada aparece na matriz.
    int,list->int"""
    n=0
    for i in range(len(mariz)):
        for j in range(len(matriz)):
            if numero==j:
                n=n+1
    return n