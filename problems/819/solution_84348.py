def filtraMultiplos(lista, n):
    nlista = []
    for x in range(len(lista)):
        if lista[x]%n == 0:
            nlista.append(lista[x])
    return nlista