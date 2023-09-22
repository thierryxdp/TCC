def melhor_volta(matriz):
    voltas = []
    for corredor in matriz:
        voltas.append(min(corredor))
    melhor = min(voltas)
    corredor = voltas.index(melhor)
    volta = matriz[corredor].index(melhor)
    return corredor+1, melhor, volta+1