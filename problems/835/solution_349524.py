def melhor_volta(matriz:list) -> tuple:
    """comentário"""
    corredores = []
    tempos = []
    for i in range(len(matriz)):
        tempos.append(min(matriz[i]))
        volta = matriz[i].index(min(matriz[i])) + 1
        corredores.append((i+1, min(matriz[i]), volta))
    melhor_volta = corredores[tempos.index(min(tempos))]
    return melhor_volta