def conta_numero(numero,matriz):
    """
    dado um numero inteiro e uma matriz de inteiros de tamanho qualquer,
    retorna quantas vezes aquele numero aparece na matriz;
    int,list->int
    """
    ind=0
    if matriz==[]:
        return 0
    linhas=len(matriz)
    colunas=len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j]==numero:
                ind+=1
    return ind