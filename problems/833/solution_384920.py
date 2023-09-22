def conta_numero(n,matriz):
    cont=0
    for i in len(matriz):
        for j in len(matriz[0]):
            if n in len(matriz):
                cont +=1
    return cont