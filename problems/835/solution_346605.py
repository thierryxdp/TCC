def coisa(matriz):
    minimos = []
    for corredores in matriz:
        minimo_local = min(corredores)
        minimos.append(minimo_local)
    minimo = min(minimos)
    for linhas in matriz:
        if minimo in linhas:
            volta = linhas.index(minimo)
            corredor = matriz.index(linhas)
    return volta,minimo,corredor