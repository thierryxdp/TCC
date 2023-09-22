def filtra_pares(tupla):
    a, b, c, d = tupla
    numero = tupla.pop(0)
    if numero % 2 == 0:
        pares.append(numero)
        pares = pares
        return pares