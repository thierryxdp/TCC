def conta_numero(numero,matriz):
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j==numero:
                contador=contador+1
    contador
    return contador