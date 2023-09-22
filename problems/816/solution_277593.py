def maiores(lista, n):
    maiores_numeros = list()
    for i in lista:
        if i >= n:
            maiores_numeros.append(i)
    return maiores_numeros