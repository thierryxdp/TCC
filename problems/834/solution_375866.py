def media_matriz(matriz):
    '''Função que, dada uma matriz, retorna a média de todos os seus números.
    list --> float'''
    soma = 0
    for x in matriz:
        for y in x:
            soma = soma + y
    return round(soma/(len(matriz)*len(x)),2)