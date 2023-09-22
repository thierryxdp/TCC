def melhor_volta(matriz):
    final = []
    for x in range(len(matriz)):
        list.append(final, min(matriz[x]))
        melhor= list.index(final, min(final))
        tempo= min(final)
        volta= list.index(matriz[melhor], tempo)
    return melhor+1, tempo, volta