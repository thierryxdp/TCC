def media_matriz(matriz):
    '''
Função que dada uma matriz de números inteiros, retorna a média de todos os números da matriz.

list--> float
    '''
    media=[]
    for i in range (len(matriz)):
        
        for coluna in range (len(matriz[0])):
            media= media+matriz[i][j]
        mediaN= sum(media)/len(matriz)* len(matriz[0])
        return round(mediaN,2)