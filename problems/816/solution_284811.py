def maiores(lista, n):
    maiores_numeros = list()
    for c in lista:
        if c >= n:
            maiores_numeros.append(c)
            
    return sorted(maiores_numeros)