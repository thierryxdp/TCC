def conta_numero(numero,matriz):
    """função que recebe uma matriz e um número
       e retorna quantas vezes esse numero 
       aparece na matriz
       int,list->int"""
    if matriz==[]:
        return 0
    nlin=len(matriz)
    ncol=len(matriz[0])
    elemento=0
    for i in range(nlin):
        for j in range(ncol):
            if numero== matriz[i][j]:
                elemento=elemento+1
    return elemento