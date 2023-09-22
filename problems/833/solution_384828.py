def conta_numero(numero,matriz):
    contador=0
    for i in matriz:
        for k in i:
            if k==numero:
                contador+=1
    return contador