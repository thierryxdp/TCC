#Start your python function here
def filtra_pares(elementos):
    pares = ()
    if elementos[0] % 2 == 0:
        pares = pares + (elementos[0],)
    if elementos[1] % 2 == 0:
        pares = pares + (elementos[1],)
    if elementos[2] % 2 == 0:
        pares = pares + (elementos[2],)
    if elementos[3] % 2 == 0:
        pares = pares + (elementos[3],)
    return pares