def conta_numero(numero,matriz):
    contador=0
    for l in matriz:
        indice=0
        for c in matriz[indice]:
            if numero==c:
                contador=contador+1
        indice=indice+1
    return contador