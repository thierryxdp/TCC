def melhor_volta(corredores):
    """Recebe uma matriz com o tempo em segundos das 10 voltas de 6 corredores.
    Retorna uma tupla informando quem obteve o melhor tempo, o tempo e em qual
    areas.
    list -> tuple"""
    melhor_tempo = 999999999999
    for corredor in corredores:
        if min(corredor) < melhor_tempo:
            melhor_tempo = min(corredor)
            melhor_corredor = list.index(corredores, corredor) + 1
            volta = list.index(corredor, min(corredor))
    return melhor_corredor, melhor_tempo, volta+1