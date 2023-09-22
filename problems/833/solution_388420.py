def conta_numero(numero,matriz):
    contador=0
    for i in range(len(matriz)):
        for x in matriz[i]:
            if numero==matriz[i][x]:
                contador+=1
    return contador