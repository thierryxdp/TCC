def conta_nummero(numero,matriz):
    contador=0
    for i in range(len(matriz)):
        if numero in matriz[i]:
            contador+=1
    return contador