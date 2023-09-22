def faltante(lista):
    falta = ()
    for e in lista:
        if e in range(1, e + 1):
            falta = falta
        else:
                falta = falta + e
    return falta