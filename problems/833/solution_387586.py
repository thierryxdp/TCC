def conta_numero(numero,matriz):
    num=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero in matriz[0]:
                num= num + 1
    return