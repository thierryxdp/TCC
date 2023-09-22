def melhor_volta(matriz):
    melhor_tempo = 0
    for corredor in range(len(matriz)):
        if min(matriz[corredor]) > melhor_tempo:
            melhor_tempo = min(matriz[corredor])
            melhor_corredor = corredor
            melhor_volta = matriz[corredor].index(melhor_tempo)
    return melhor_corredor+1,melhor_tempo,melhor_volta+1