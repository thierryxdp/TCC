def conta_numero(numero,matriz):
    '''função que dados um numero inteiro e uma matriz, retorna
    a quantidade de vezes que numero aparece na matriz
    int,list->list'''
    if matriz==[] and numero==0:
                return 0
    qtas_vezes=0
    linhas=len(matriz)
    colunas=len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j]==numero:
                qtas_vezes+=1
    return qtas_vezes