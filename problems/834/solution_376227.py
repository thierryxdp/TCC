def media_matriz(matriz):
    ''' Função que,dada uma matriz de inteiros não vazia, retorna a
    média de todos os números da matriz.
    list(list)-->float'''
    mediaparcial = 0
    media = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            mediaparcial = (matriz[i][j])/(len(matriz)*len(matriz[0]))
            media = media + mediaparcial
    return round(media,2)