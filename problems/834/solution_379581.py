def media_matriz(matriz):
    '''
Função que dada uma matriz de números inteiros, retorna a média de todos os números da matriz.

list--> float
    '''
    media=[]
    for i in len(matriz):
        for coluna in len(matriz[0]):
            media.append(coluna)
        mediaN= sum(media)/len(media)
        return round(mediaN,2)