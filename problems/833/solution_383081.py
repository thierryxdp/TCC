def conta_numero(matriz,numero):
    cont = 0
    for elemento in matriz:
        if elemento == numero:
            cont += 1
    return cont