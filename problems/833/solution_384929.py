def conta_numero(n,matriz):
    cont=0
    for n in range(len(matriz)):
        if n in matriz:
            cont+=1
    return cont