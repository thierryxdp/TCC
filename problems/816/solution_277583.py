def maiores(lista, n):
    maiores_numeros = list()
    for i in lista:
        if i >= n:
            maiores_numeros.insert(maiores_numeros,0,i)
    return maiores_numeros