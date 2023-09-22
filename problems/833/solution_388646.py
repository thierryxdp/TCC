def conta_numero(numero,matriz):
    count = 0
    for n in matriz:
        count+=n.count(numero)
    return count