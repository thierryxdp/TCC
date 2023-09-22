def conta_numero(numero,matriz):
    cont = 0
    for i in matriz:
        cont += i.count(n)
    return cont