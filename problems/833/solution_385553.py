def conta_numero(matriz,num):
    contador=0
    for i in range(len(matriz)):
        contador+=matriz[i].count(num)
    return contador