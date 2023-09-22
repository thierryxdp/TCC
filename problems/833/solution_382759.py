def conta_numero(numero,matriz):
    contador=0
    for l in matriz:
        for c in matriz[l]:
            if numero==c:
                contador=contador+1
    return contador