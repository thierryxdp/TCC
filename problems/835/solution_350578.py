def melhor_volta(M):
    tempos = []
    for i in range(7):
        tempos = tempos + [M[i]]
        menor_tempo = min(tempos)
    return menor_tempo