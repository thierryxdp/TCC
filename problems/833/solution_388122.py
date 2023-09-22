def conta_numero(numero,matriz):
    conta=0
    for i in range(len(matriz)):
        conta=conta+list.count(matriz[i],numero)
    return conta