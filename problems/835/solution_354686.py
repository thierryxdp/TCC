def melhor_volta(matriz):
    """Função que retorna uma tupla informando de quem foi a melhor volta, com qual tempo e em que volta
    list -> tuple"""
    i = 0
    melhor_tempo_corredor = []
    melhor_volta_corredor = []
    while i < 6:
        melhor_tempo = min(matriz[i])
        melhor_tempo_corredor += [melhor_tempo,]
        melhor_lap = matriz[i].index(melhor_tempo)
        melhor_volta_corredor += [melhor_lap,]
        i += 1
    tempo = min(melhor_tempo_corredor)
    piloto = melhor_tempo_corredor.index(tempo)
    volta = melhor_volta_corredor[piloto]
    return (piloto+1,tempo,volta+1)