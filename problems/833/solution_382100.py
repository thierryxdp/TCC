def conta_numeros(numero,matriz):
    cont=0
    for i in range len(matriz):
        for j in range len(matriz[0]):
            if numero==i:
                cont=cont+1
            if numero==j:
                cont=cont+1
    return cont