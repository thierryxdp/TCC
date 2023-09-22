def conta_numero(numero, matriz):
    contador = 0
    while numero in matriz:
        contador = contador + 1
    return contador