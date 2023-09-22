def media_matriz(matriz):
    contador = 0
    acumulador = 0

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            acumulador += matriz[linha][coluna]
            contador += 1

    return round((acumulador/contador),2)