def media_matriz(m):
    ''' retorna a média de todos os números da matriz m de inteiros não vazia;
    mat -> float '''
    x = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            x = x + m[i][j]
    media = x/(len(m)*len(m[0]))
    return round(media,2)