def conta_numero(numero,matriz):
    num=0
    for i in len(matriz):
        for j in len(matriz[0]):
            if numero in matriz[0]:
                num+=1
    return num