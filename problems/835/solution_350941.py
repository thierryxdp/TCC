def melhor_volta(matriz):
    ''''''
    for corredor in matriz:
            melhor_volta=min(corredor)
            melhor_tempo=corredor[list.index(melhor_volta)]
            melhor_corredor=matriz[list.index(melhor_tempo)]
    return tuple(melhor_corredor,melhor_tempo,melhor_volta)