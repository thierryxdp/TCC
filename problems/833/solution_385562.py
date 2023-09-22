def conta_numero(numero,matriz):
    freq=0
    for i in range(len(matriz)):
        for numero in matriz[i]:
            freq=freq+1
    return freq