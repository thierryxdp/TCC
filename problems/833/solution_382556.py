def conta_numero(numero,matriz):
    for i in matriz:
        if numero in matriz[0]:
            return list.count(matriz[0],numero)
        if numero in matriz[1]:
            return list.count(matriz[1],numero)
        if numero in matriz[3]:
            return list.count(matriz[3],numero)
        if numero in matriz[5]:
            return list.count(matriz[5],numero)
        else:
            return 0