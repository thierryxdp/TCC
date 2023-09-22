#Start your python function here
def filtra_pares(num_tupla):
    pares = []

    if len(num_tupla) > 0:
        numero = num_tupla.pop(0)
        if numero % 2 == 0:
            pares.append(numero)
        pares = pares + filtra_pares(num_tupla)
    return pares