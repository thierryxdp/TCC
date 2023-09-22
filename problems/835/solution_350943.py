def melhor_volta(matriz):
    ''''''
    for corredor in matriz:
            melhor_volta=min(corredor)
            melhor_tempo=list.index(corredor,melhor_volta)
            melhor_corredor=list.index(corredor,melhor_tempo)
    return tuple(melhor_corredor,melhor_tempo,melhor_volta)