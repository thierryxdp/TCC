def filtra_pares(tupla):
    pares = ()
    numero = tupla.pop(0)
    if numero % 2 == 0:
        pares.append(numero)
        return pares