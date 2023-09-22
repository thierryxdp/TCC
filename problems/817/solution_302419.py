def acima_da_media(lista, n):
    nlista = []
    for x in lista:
        if x > n:
            nlista.append(x)
    nlista.sort()
    return nlista