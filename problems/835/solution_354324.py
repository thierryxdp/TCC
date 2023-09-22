def melhor_volta(matriz):
    """Retorna uma tupla com o melhor tempo de volta, o piloto responsável e em qual volta;
    list -> tuple"""
    i = 0
    melhor_tempo_corredor = []
    melhor_volta_corredor = []
    while i < 6:
        melhor_tempo_corredor += [min(matriz[i]),]
        melhor_volta_corredor += [matriz[i].index(melhor_tempo_corredor[i]),]
        i += 1
    tempo = min(melhor_tempo_corredor)
    piloto = melhor_tempo_corredor.index(tempo)
    volta = melhor_volta_corredor[piloto]
    return (piloto+1,tempo,volta+1)