def maiores(lista, n):
    maiores_numeros = list()
    for i in lista:
        if i >= n:
            maiores_numeros.insert(i,0,0)
    return maiores_numeros