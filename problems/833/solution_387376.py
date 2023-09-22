def conta_numero(numero,matriz):
    contador=2
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j==numero:
                contador=contador+1
    return contador