def soma_h(n):
     
    indice = 0
    for i in range(1, n + 1):
        matrizInversa = (1/i)
        indice += matrizInversa
    return round(indice, 2)