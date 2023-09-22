def conta_numero(numero,matriz):
    count=0
    for n in matriz:
        count+=matriz.count(numero)
    return count