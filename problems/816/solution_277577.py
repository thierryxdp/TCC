def maiores(lista, n):
    maiores_numeros = lista()
    for i in lista:
        if i >= n:
            maiores_numeros.append(i)
    return maiores_numeros