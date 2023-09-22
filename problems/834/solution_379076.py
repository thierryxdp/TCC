def media_matriz(m):
    '''Retorna a média de todos os números da matriz.
    list(list)->float)'''
    linhas=len(m)
    colunas=len(m[0])
    quant_elem=linhas*colunas
    soma=0
    for i in range(linhas):
        for j in range(colunas):
            soma=soma+m[i][j]
    return soma/quant_elem