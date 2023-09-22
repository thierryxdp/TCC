def faltante(lista):
    completa = range(1, max(lista) + 1)
    i = 0
    while i < len(completa) - 1:
        if completa[i] not in lista:
            return completa[i]
        i += 1
    return completa[i] + 1