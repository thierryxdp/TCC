def conta_numero(matriz,numero):
    cont = 0
    for lista in matriz:
        for elemento in lista:
            if elemento == numero:
               cont = cont + 1
    return cont