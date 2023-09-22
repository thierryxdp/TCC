def conta_numero(numero,matriz):
    for i in matriz:
        if numero in matriz[0]:
            return list.count(matriz[0],numero)