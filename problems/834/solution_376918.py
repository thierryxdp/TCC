def media_matriz(matriz):
    ''' depois de repartir e saber o inicio e fim da string
    usando a função round para arredondar para o mais próximo número'''
    Media=0
    for i in range(len(matriz)):
        for c in range(len(matriz[0])):
            Media=Media+matriz[i][c]
    return round(Media/(len(matriz)*len(matriz[0])),2)