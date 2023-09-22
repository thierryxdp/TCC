def conta_numero(numero,matriz):
    m=len(matriz[0])
    if numero in matriz[0]:
        return m-numero
    else:
        return 0