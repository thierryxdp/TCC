def media_matriz(matriz):
    ''' dado duma matriz como entrada calcula e retorna a media de todos numeros dessa matriz
list->float'''
    soma = 0
    for i in matriz:
        for j in i:
            soma = soma + j
    y = len(matriz)*len(matriz[0])    
    return round(soma/y, 2)