def melhor_volta(matriz:list) -> tuple:
    """comentário"""
    melhores = []
    tempos = []
    for i in range(len(matriz)):
        tempos.append(min(matriz[i]))
        volta = matriz[i].index(min(matriz[i])) + 1
        melhores.append((i+1, min(matriz[i]), volta))
    melhor_volta = melhores[tempos.index(min(matriz[i]))]
    return melhor_volta