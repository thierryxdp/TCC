def conta_numero(numero,matriz):
    ''' recebe um numero e uma matriz e conta quantas vezes aquele numero aparece na matriz
    int,list(list)->int'''
    linhas= len(matriz)
    colunas= len(matriz[0])
    qtd_vezes= 0
    if matriz == []:
        qtd_vezes= 0
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == numero:
                qtd_vezes= qtd_vezes + 1
    return qtd_vezes