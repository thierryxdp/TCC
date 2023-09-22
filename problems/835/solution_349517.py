def melhor_volta(matriz:list) -> tuple:
    """comentário"""
    tempos = []
    for i in range(len(matriz)):
        tempos.append((i+1, min(matriz[i]),matriz[i].index(min(matriz[i])+1)))
    return tempos