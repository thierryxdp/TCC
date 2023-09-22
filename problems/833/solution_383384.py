def conta_numero(numero,matriz):
    aux=0
    for i in range(len(matriz)):
        aux=aux+list.count(matriz[i], numero)
    return aux