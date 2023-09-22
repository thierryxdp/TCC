def media_matriz(m):
    '''função que, dada uma matriz de inteiros não vazia,retorna
    a média de todos os números da matriz; list -> float'''
    qntd_numeros=len(m)*len(m[0])
    c=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            c=c+m[i][j]
    media=c/qntd_numeros
    return round(media,2)