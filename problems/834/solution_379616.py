def media_matriz(matriz):
    '''
Função que dada uma matriz de números inteiros, retorna a média de todos os números da matriz.

list--> float
    '''
    media=0
    for i in range (len(matriz)):
        for j in range (len(matriz[0])):
            media+=[i][j]
    total= media/len(matriz)*len(matriz[0])
    
    return round(mediaN,2)