def filtraMultiplos(lista, n):
    m = []
    for e in lista:
        if e%n == 0:
            m.append(e)
    return m