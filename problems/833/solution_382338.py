def conta_numero(numero,matriz):
    for numero not in matriz:
        return 0
    for i in range(len(matriz)):
        quantidade=list.count(matriz[i], numero)
    return quantidade