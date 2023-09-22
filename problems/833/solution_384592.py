def conta_numero(numero,matriz):
    a=0
    for i in range(len(matriz)):
        a=a+list.count(matriz[i],numero)
    return a