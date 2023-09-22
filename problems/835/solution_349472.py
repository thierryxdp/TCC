def melhor_volta(m):
    corredores = 0
    tempo = 1000
    voltas = 0
    for lista in range(len(m)):
        if min(matriz[lista]) < tempo:
            tempo = min(matriz[lista])
            corredores = lista + 1
            voltas = list.index(min(matriz[lista])) + 1
    return (corredores, tempo, voltas)