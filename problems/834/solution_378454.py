def media_matriz(mat):
    '''função que dada uma matriz de inteiros não vazia,
    retorna a média de todos os números da matriz'''
    lin = len(mat)
    col = len(mat[0])
    i = 0
    soma = 0
    while i < lin:
        soma = soma + sum(mat[i])
        i = i + 1
    return round(soma/(lin*col),2)