def conta_numero(numero, matriz):
    indice=0
    while indice < len(matriz):
        contador=0
        if numero in matriz[indice]:
            contador=contador+1
        indice=indice+1
    return contador