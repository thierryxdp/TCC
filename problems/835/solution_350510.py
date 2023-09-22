def melhor_volta(matriz):
    corredor = 0
    melhor_tempo = 100000000000
    for linha in matriz:
        if min(linha) < melhor_tempo:
            melhor_tempo = min(linha)
            corredor = matriz.index(linha) + 1
            volta = linha.index(melhor_tempo) + 1
    return corredor, melhor_tempo, volta