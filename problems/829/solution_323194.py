def soma_h(n):
    # Função que dado um número o valor h
    # int -> float
    indice = 0
    for i in range(1, n + 1):
        matrizInversa = (1/i)
        indice += matrizInversa
    return round(indice, 2)