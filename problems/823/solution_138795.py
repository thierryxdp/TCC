def faltante(lista):
    falta = ()
    for e in lista:
        if e not in range(1, e + 1):
            falta = falta + e
        else:
                falta = falta
    return falta