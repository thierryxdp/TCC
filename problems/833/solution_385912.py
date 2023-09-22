def conta_numero(numero,matriz):
    ''''''
    for elemento in matriz:
        if numero in elemento:
            return list.count(elemento,numero)
        else:
            return 0