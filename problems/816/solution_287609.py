def maiores(lista, n):
    nlista = []
    for x in range(len(lista)):
        if lista[x] > n:
            nlista += lista[x]
    return list.sort(nlista)