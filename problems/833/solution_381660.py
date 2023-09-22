def conta_numero(numero, matriz):
    indice=0
    contador=0
    digito=matriz[indice]
    while indice < len(matriz):
        j=0
        while j<len(digito):
            if numero==digito[j]:
                contador=contador+1
            j=j+1
        indice=indice+1
    return contador