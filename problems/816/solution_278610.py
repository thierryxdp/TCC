def maiores(lista, n):
    numeros_maiores = list()
    for x in lista:
        if x >= n:
            numeros_maiores.append(x)
    return numeros_maiores