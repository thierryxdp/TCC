def filtra_pares(*args):

    i=0
    lista=""
    for arg in args:
        lista = lista + str(arg)

    a = int(lista[0])
    b = int(lista[1])
    c = int(lista[2])
    d = int(lista[3])



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

(f(1,5,8,4))