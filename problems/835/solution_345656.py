def melhor_volta(matriz):
    """Determina o menor tempo dentre vários corredores em uma corrida"""
    media = []
    m = len(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            elemento = matriz[i][j]
            list.append(media,elemento)
    return (min(media))