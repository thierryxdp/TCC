def conta_numero(numero,matriz):
    i=0
    for i in range(len(matriz)):
        quantidade=matriz[i].count(numero)
        i+=1
    return quantidade