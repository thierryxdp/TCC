def media_matriz(matriz):
    '''função que dada uma matriz de inteiros não vazia,retorna a media de todos os numeros; int,list->float'''
    soma = 0
    for n in range(len(matriz)):
        for i in range(len(matriz[n])):
            soma += matriz[n][i]
    return round(soma/(len(matriz)*len(matriz[0])),2)