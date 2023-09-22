def conta_numero(numero,matriz):
    cont = 0
    for i in matriz:
        for j in i:
            if numero == j:
                cont = cont + 1
    return cont