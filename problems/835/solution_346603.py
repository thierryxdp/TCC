def melhor_volta(matriz):
    minimos = []
    contador = 0
    for linhas in matriz:
        minimo_local = min(linhas)
        minimos.append(minimo_local)
    for linhas2 in matriz:
        contador += 1
        if min(minimos) in linhas2:
            return contador,linhas2.index(min(minimos)),min(minimos)