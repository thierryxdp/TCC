def conta_numero(numero,matriz):
    contador=0
    for i in matriz:
        for j in matriz[len(i)-1]:
            if numero in matriz[len(i)-1]:
                contador=contador+1
    return contador