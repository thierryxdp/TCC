def conta_numero(numero,matriz):
    contador=0
    for i in matriz:
        for j in i:
            if numero in i:
                contador=contador+1
            else:
                contador=contador+0
                
    return contador