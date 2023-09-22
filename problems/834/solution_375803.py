def media_matriz(A):
    '''dada uma matriz A retorna a media de todos os elementos'''
    soma = 0
    contador = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            soma = soma + A[i][j]
            contador = contador + 1
    return round(soma/contador)