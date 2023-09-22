def conta_numero(numero,matriz):
    repetiu = 0
    for indice in range(0, len(matriz)):
        repetiu+=1 
        if matriz[indice] == numero:
            repetiu += 1
        else:
            repetiu == 0
    return repetiu