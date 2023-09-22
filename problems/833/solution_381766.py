def conta_numero(numero,matriz):
    contador=0
    indice=0
    while indice<len(matriz):
        for elemento in len(matriz[0]):
            if numero==elemento:
                contador=contador+1
        indice=indice+1
    return contador