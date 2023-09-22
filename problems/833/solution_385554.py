def conta_numero(numero,matriz):
    contador=0
    for i in range(len(matriz)):
        contador+=matriz[i].count(numumero)
    return contador