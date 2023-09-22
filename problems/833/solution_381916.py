def conta_numero(numero,matriz):
    vezes=0
    for c in range(len(matriz)):
        if numero in matriz[c]:
            vezes=vezes+matriz[c].count(numero)
    return vezes