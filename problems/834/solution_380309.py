def media_matriz(matriz):
    '''Retorna a média de todos os números da matriz.
    list->float'''
    soma=0
    for i in matriz:
        for j in i:
            soma+=j
        
    return  round(soma/((len(matriz))*(len(matriz[0])),2)