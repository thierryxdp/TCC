def conta_numero(numero, matriz):
    contador = 0
    for linha in matriz:
        for coluna in matriz:
            contador = list.count(matriz,coluna)
        contador = contador + 1
    return contador