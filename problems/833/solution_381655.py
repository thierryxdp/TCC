def conta_numero(numero, matriz):
    indice=0
    contador=0
    digito=matriz[indice]
    while indice < len(matriz):
        for elemento in digito:
            if numero==digito:
                contador=contador+1
        indice=indice+1
    return contador