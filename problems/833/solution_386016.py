def conta_numero(numero,matriz):
    q = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
                       if j == numero:
                       	q+=1
    return q