def conta_numero(numero, matriz):
    cont = 0
    for numero in matriz:
        for num in numero:
            if num == 2:
            cont += 1
    return cont