def conta_numero(numero, matriz):
    contador = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if (matriz[linha][coluna] == numero):
                contador += 1
    return contador