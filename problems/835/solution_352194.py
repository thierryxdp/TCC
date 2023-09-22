def melhor_volta(matriz):
    tempos = []
    volta_numero = []
    for C in matriz:
        melhor_tempo = min(C)
        list.append(tempos, melhor_tempo)
        N =list.index(C, min(C))
        list.append(volta_numero, N)
    M = list.index(tempos, min(tempos))
    T = ((M + 1), min(tempos), volta_numero[M])
    return T