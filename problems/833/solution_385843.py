def conta_numero(numero, matriz):
    x=0
    e = 0
    while x < len(matriz):

        for i in matriz[x]:

            if i == numero:
                #if i :
                e += +1
        x += +1
    return e