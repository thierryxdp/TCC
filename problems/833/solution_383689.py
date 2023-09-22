def conta_numero(numero,matriz):
    cont = 0
    for x in matriz:
        for y in range(len(x)):
            if x[y] == numero:
            	cont  += 1
    return cont