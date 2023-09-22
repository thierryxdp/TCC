def maiores(lista, n):
    maiores_numeros = list()
    for i in lista:
        if i >= n:
            maiores_numeros.extend(i)
            return maiores_numeros