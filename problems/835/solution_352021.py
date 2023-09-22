def melhor_volta(mat):
    """Recebe uma matriz que contém os tempos referentes
a cada volta de cada corredor de kart. Retorna uma tupla
contendo o número do corredor que teve a melhor volta (int),
o tempo dessa volta (int) e o número dessa volta (int).
Obs: o número dos corredores e das voltas começam em 1,
apesar de índices em Python começarem em 0.
mat -> tuple
"""    
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