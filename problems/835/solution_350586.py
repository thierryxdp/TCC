def melhor_volta(M):
    tempos = []
    for i in range(6):
        tempos = tempos + M[i]
    return min(tempos)