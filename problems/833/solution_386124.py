def conta_numero(numero,matriz):
    for n in matriz:
        while n == numero:
            return matriz.count(numero)