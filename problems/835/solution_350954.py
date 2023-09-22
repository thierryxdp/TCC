def melhor_volta(mat):
    melhor_kart = melhor_tempo = melhor_volta = 0
    for k, ts in enumerate(mat, 1):
        if min(ts) < melhor_tempo:
			melhor_kart = k
            melhor_tempo = min(ts)
            melhor_volta = list.index(ts)
    return melhor_kart, melhor_tempo, melhor_volta