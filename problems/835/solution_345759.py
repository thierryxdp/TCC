def melhor_volta(matriz):
    '''Função que recebe como entrada uma matriz 6 × 10 com os tempos em segundos dos
    corredores em cada volta. A função retorna tupla informando quem teve a melhor volta.
    list -> tupla'''
    minimo = []
    for n in range(len(matriz)):
        minimo += [min(matriz[n])]
    melhor =list.index(minimo,min(minimo))
    volta = list.index(matriz[melhor],min(minimo))
    return melhor+1,min(minimo),volta+1