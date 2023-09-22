def media_matriz(matriz):
    '''
Função que dada uma matriz de números inteiros, retorna a média de todos os números da matriz.

list--> float
    '''
    media=[]
    for i in matriz:
        qtd=0
        for coluna in lINHA:
            media.append(coluna)
        mediaN= sum(media)/len(media)
        return round(mediaN,2)