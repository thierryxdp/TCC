def maiores(lista,n):
    nlista = []
    for x in lista:
        if x > n:
            nlista.append(x)
        nlista.sort(x)
        return lista