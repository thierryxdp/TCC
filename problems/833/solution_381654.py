def conta_numero(numero, matriz):
    indice=0
    contador=0
    while indice < len(matriz):
        if numero in matriz[indice]:
            contador=contador+1
        indice=indice+1
    return contador