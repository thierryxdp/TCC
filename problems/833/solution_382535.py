def conta_numero(numero,matriz):
    for i in matriz:
        if numero in matriz:
            return matriz.count(numero)
        else:
            return 0