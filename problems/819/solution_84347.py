def filtraMultiplos(lista, n):
    nlista = []
    while x < len(lista):
        if lista[x]%n == 0:
            nlista.append(lista[x])
    return nlista