def melhor_volta(matriz:list) -> tuple:
    """comentário"""
    tempos = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            tempos += ([i, min(matriz[i]), j])
    return tempos