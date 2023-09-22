def melhor_volta(matriz):
    """Retorna uma tupla com o melhor tempo de volta, o piloto responsável e em qual volta;
    list -> tuple"""
    i = 0
    melhor_tempo = []
    melhor_voltaa = []
    while i < 6:
        j = 0
        melhor_tempo[i] = 9999999999
        melhor_voltaa[i] = 0
        while j < 10:
            if matriz[i][j] <= melhor_tempo[i]:
                melhor_tempo[i] = matriz[i][j]
                melhor_voltaa[i] = j
            j += 1
        i += 1
    tempo = min(melhor_tempo)
    piloto = melhor_tempo.index(tempo)
    volta = melhor_voltaa[piloto]
    return (piloto,tempo,volta)