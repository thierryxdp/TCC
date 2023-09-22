def media_matriz(m):
    '''Função que dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz
       matriz->float'''
    s = 0
    nova_matriz = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            s = s + m[i][j]
            nova_matriz = nova_matriz + 1
    media = s / nova_matriz
    return round(media,2)