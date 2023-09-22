def conta_numero(numero, matriz):
    contador = 0
    for numero in range (len(matriz)):
        if numero == matriz[numero]:
            contador += 1
    return contador