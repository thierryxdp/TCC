def conta_numero(numero,matriz):
    for i in matriz:
        if numero in matriz:
            return list.count(matriz[1],numero)
        else:
            return 0