def maiores(lista, n):
    maiores_numeros = list()
    maiores_numeros.sort()
    for c in lista:
        if c > n:
            maiores_numeros.append(c)
    return maiores_numeros