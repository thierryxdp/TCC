def media_matriz(matriz):
    ''' recebe uma matriz e calcula a media de seus numeros
    list(list)->float'''
    colunas= len(matriz[0])
    linhas= len(matriz)
    qtd_numeros = 0
    soma= 0
    for i in range(linhas):
        for j in range(colunas):
            soma = soma + matriz[i][j]
            qtd_numeros= qtd_numeros + 1
    return soma/qtd_numeros