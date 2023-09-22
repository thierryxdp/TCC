def maiores(lista, n):
    maiores_numeros = list()
    for c in lista:
        if c >= n:
            maiores_numeros.append(c)
    list.sort(maiores_numeros)
    return maiores_numeros