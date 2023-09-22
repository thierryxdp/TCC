def conta_numero(numero,matriz):
    contador=0
    contador2=0
    for i in matriz:
        for j in i:
            if numero in i:
                contador=contador+1
        contador2=contador2+1
    return contador