def media_matriz(mat):
    '''Recebe uma matriz não vazia composta por números
    inteiros e retorna a média de seus elementos.
    list -> float'''
    elementos = len(mat[0])*len(mat)
    soma = 0
    for linha in mat:
        for numero in linha:
            soma += numero
    media = soma/elementos
    return round(media,2)