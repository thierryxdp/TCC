def media_matriz(m):
    """a função recebe uma matriz não vazia e retorna a media de todos os
    numeros da matriz;
    list->float"""
    soma = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            componentes = len(m) * len(m[0])
            soma = soma + m[i][j]
    media = soma/componentes
    return round(media,2)