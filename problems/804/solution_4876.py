#Start your python function here
def filtra_pares(a,b,c,d):
    tupla = (a,b,c,d)

    pares = ""

    if a%2 == 0:
        pares = pares + str(tupla[0]) + ','
    if b%2 == 0:
        pares = pares + str(tupla[1]) + ','
    if c%2 == 0:
        pares = pares + str(tupla[2]) + ','
    if d%2 == 0:
        pares = pares + str(tupla[3])

    x = pares.split(',')
    y = tuple(x)

    return y