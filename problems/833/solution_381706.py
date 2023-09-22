def conta_numero(numero,matriz):
    contador=0
    for i in matriz:
        for j in matriz[len(i)]:
            if numero in matriz[len(i)]:
                contador=contador+1
    return contador