def melhor_volta(mat):
    tempos = []
    for voltas in mat:
        list.append(tempos, min(voltas))
    melhor_tempo = min(tempos)
    i = 0
    for voltas in mat:
        i = i + 1
        if melhor_tempo in voltas:
            melhor_kart = i
            melhor_volta = list.index(voltas, melhor_tempo) + 1
    return melhor_kart, melhor_tempo, melhor_volta