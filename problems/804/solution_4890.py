def filtra_pares(*args):
    i=0
    lista=""
    for arg in args:
        lista = lista + str(arg)

    a = lista[0]
    b = lista[1]
    c = lista[2]
    d = lista[3]

    a = float(float(a))
    b = float(float(b))
    c = float(float(c))
    d = float(float(d))

    pares = ""

    if a%2 == 0:

        pares = pares + str(lista[0]) + ','
    if b%2 == 0:
        pares = pares + str(lista[1]) + ','
    if c%2 == 0:
        pares = pares + str(lista[2]) + ','
    if d%2 == 0:
        pares = pares + str(lista[3])

    x = pares.split(',')
    y = tuple(x)

    return y

filtra_pares(1,2,3,4)