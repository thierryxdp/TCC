def conta_numero(numero,matriz):
    vezes=0
    i=0
    for c in range(len(matriz)):
        if numero in matriz[c][i]:
            vezes=vezes+1
            i=i+1
    return vezes