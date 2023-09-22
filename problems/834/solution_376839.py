def media_matriz(m):
    """
    Retorna a media dos numeros da matriz
    list -> float
    """
    linhas=len(m)
    colunas=len(m[0])
    soma=0
    for i in range(linhas):
        for j in range(colunas):
            soma=soma+m[i][j]
    media=soma/(linhas*colunas)
    return media