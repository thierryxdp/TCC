def conta_numero(numero,matriz):
    total = 0
    for i in matriz:
        total = total + i.count(numero)
    return total