def media_matriz(m):
    '''funçao que dada uma matriz de inteiros não vazia, retorna a média de todos os números
    da matriz; list->int'''
    x = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            x=x+m[i][j]
        media=x/((len(m))*len(m[0])))
    return round(media,2)