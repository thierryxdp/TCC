def filtra_pares(tupla):
    pares = []
    if len(tupla) > 0:

        numero = tupla.pop(0)

        if numero % 2 == 0:

            pares.append(numero)

        pares = pares + filtra_pares(tupla)

    return tuple(pares)