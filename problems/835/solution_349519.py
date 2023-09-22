def melhor_volta(matriz:list) -> tuple:
    """comentário"""
    tempos = []
    for i in range(len(matriz)):
        volta = matriz[i].index(min(matriz[i])) + 1
        tempos.append((i+1, min(matriz[i]), volta))
    return tempos