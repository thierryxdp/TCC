def conta_numero(numero,matriz):
    resultado=0
    for valor in range(len(matriz[0])):
        if matriz[0][valor]==numero:
            resultado=1+resultado
    return resultado