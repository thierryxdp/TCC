def media_matriz(matriz):
    '''Funcao que dada uma matriz de inteiros nao vazia, retorna a media de todos 
    os numeros da matriz.'''
    media = 0
    for linha in matriz:
        for elemento in linha:
            media = media + elemento
            conta = media/(len(matriz)*len(matriz[0]))
            return round(conta,2)