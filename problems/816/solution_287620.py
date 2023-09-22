def maiores(lista, n):
    nlista = []
    for x in lista:
        if x > n:
            nlista.append(x)
    return list.sort(nlista)