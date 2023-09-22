def conta_numero(numero,matriz):
    conta=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            conta=conta+list.count(matriz[i],numero)
    return conta