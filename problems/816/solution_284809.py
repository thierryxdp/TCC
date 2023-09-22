def maiores(lista, n):
    maiores_numeros = lista()
    for c in lista:
        if c >= n:
            maiores_numeros.append(c)
    return maiores_numeros