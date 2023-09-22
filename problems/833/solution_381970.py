def conta_numero(numero,matriz):
    resultado=0
    for valor in range(len(matriz[0])):
        if numero in range(matriz[0][valor]):
            resultado=1+resultado
    return resultado