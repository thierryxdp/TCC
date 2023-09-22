def conta_numero(numero,matriz):
    total=0
    for i in range(len(matriz)):
        quantidade=matriz[i].count(numero)
        total+=quantidade
        i+=0
        return total