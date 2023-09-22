def conta_numero(numero, matriz):
    contador = 0
    for i in matriz:
        for j in matriz:
            contador = list.count(matriz,numero)
        contador = contador + 1
    return contador