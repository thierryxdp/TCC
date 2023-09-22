def conta_numero(numero,matriz):
    c = 0
    for i in matriz:
        x = list.count(numero,matriz)
        c += x
    return c