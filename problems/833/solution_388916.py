def conta_numero(numero, matriz):
    contador = 0
    i=0
    j=0
    for i in matriz:
        for j in i:
            if j == numero:
                contador += 1
    return contador