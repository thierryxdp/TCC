def conta_numero(n,matriz):
    cont=0
    for i in range(len(matriz)):
        for j in len(matriz[0]):
            if n in range(len(matriz)):
                cont +=1
    return cont