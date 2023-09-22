def melhor_volta(matriz:list) -> tuple:
    """comentário"""
    tempos = []
    for i in range(len(matriz)):
        tempos.append(min(matriz[i]))