def conta_numero(numero,matriz):
    C=0
    for c in matriz:
        if matriz[0][c]==numero:
            C+=1
    return C