def conta_numero(numero,matriz):
    contador=0
    indice=0
    while indice<len(matriz):
        indice2=0
        while indice2<len(matriz[indice]):
            if numero==matriz[indice][indice2]:
                contador=contador+1
                indice2=indice2+1
        indice=indice+1
    return contador