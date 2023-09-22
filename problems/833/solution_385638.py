def conta_numero(num,matriz):
    """"""
    contador=0
    for i in matriz:
        for j in i:
            if num==j:
                contador=contador+1
    return contador