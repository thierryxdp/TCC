def conta_numero(numero, matriz):
    contador = 0
    for i in range (len(matriz)):
        if numero == matriz[0]:
            contador += 1
    return contador