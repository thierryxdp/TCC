def conta_numero(numero,matriz):
    cont = 0
    for lista in matriz:
        for elemento in lista:
            if elemento == numero:
               cont = cont + 1
    return cont