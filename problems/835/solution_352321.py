def melhor_volta(mat):
    """retorna quem foi o que teve melhor volta, o tempo e em qual volta ganhou."""
    melhor_kart = -1
    melhor_tempo = -1
    melhor_volta = -1
    ts = []
    for vs in mat:
        list.append (ts, min(vs))
    melhor_tempo = min(ts)
    for i,vs in enumerate(mat,1):
        if melhor_tempo in vs:
            melhor_kart = i
            melhor_volta = list.index(vs, melhor_tempo) + 1
    return melhor_kart, melhor_tempo, melhor_volta