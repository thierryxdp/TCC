def conta_numero(numero,matriz):
    for i in range(len(matriz)):
        quantidade=list.count(matriz[i], numero)
        i+=1
    return quantidade