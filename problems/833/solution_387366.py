def conta_numero(numero,matriz):
    contador=0
    for i in matriz:
        for j in matriz[i]:
            if numero==range(matriz[i]):
                contador=contador+1
    return contador