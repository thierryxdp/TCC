def conta_numero(numero,matriz):
    contador=0
    for linhas in len(matriz):
        for elemento in len(matriz[0]):
            if numero==elemento:
                contador=contador+1
    return contador