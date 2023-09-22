def media_matriz(m):
    '''Dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz'''
    soma=0
    peso=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            soma=soma+m[i][j]
            peso=peso+1
    return round(soma/peso,2)