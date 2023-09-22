def melhor_volta(matriz):
    melhores_voltas = []
    for corredores in matriz:
        melhor_volta_corre = min(corredores)
        melhores_voltas.append(melhor_volta_corre)
    melhor_tempo = min(melhores_voltas)
    for corredores in matriz:
        if melhor_tempo in corredores:
            melhor_corredor = matriz.index(corredores)+1
            melhor_volta = corredores.index(melhor_tempo)+1
    return melhor_corredor,melhor_tempo,melhor_volta