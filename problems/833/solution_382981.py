def conta_numero(numero,matriz):
    vezes = 0
    for x in len(matriz):   
        if numero in matriz[x]:
            vezes += 1
    return vezes