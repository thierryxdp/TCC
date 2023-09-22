def media_matriz(m):
    ''' Função que calcula a média de todos os números da matriz.
    list->int'''
    t=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            b=m[i][j]
            t=t+b
    media=t/(len(m)*len(m[0]))
    return round(media,2)