def maiores(lista, n):
    nlista = []
    for x in lista:
        if x > n:
            nlista.append(x)
    nlista.sort()
    return nlista

def acima_da_media(lista):
    lista = maiores(lista, 4)
    return lista