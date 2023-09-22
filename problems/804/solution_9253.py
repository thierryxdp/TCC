#Start your python function here
def filtra_pares(elementos):
    pares = ()
    if elementos[0] % 2 == 0:
        pares.append(elementos[0])
    if elementos[1] % 2 == 0:
        pares.append(elementos[1])
    if elementos[2] % 2 == 0:
        pares.append(elementos[2])
    if elementos[3] % 2 == 0:
        pares.append(elementos[3])
    return pares