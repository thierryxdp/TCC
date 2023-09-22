def melhor_volta(matriz):
    ''''''
    for corredor in matriz:
        for tempo in corredor:
            melhor_volta=min(tempo)
            melhor_tempo=tempo[list.index(melhor_volta)]
            melhor_corredor=matriz[list.index(melhor_tempo)]
    return tuple(melhor_corredor,melhor_tempo,melhor_volta)