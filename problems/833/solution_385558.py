def conta_numero(numero, matriz):
    """retorna quantas vezes número aparece na matriz;
   int, list -> int"""
    nlin = len(matriz)
    if nlin==0:
        return 0
    ncol=len(matriz[0])
    c=0
    for i in range(nlin):
        for j in range(ncol):
            if numero==matriz[i][j]:
                c=c+1
    return c