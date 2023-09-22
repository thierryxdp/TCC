def conta_numero(numero,matriz):
    contador=0
    for l in matriz:
        indice=0
        for c in matriz[indice]:
            k=list.count(matriz[indice],numero)
            contador=contador+k
        indice=indice+1
    return contador