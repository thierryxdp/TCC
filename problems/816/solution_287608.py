def maiores(lista, n):
    nlista = []
    for x in lista:
        if x > n:
            nlista += x
    return list.sort(nlista)