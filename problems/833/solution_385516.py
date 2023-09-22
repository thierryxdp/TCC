def conta_numero (numero, matriz):
    '''funcao que conta quantas vezes aquele numero aparece na matriz'''
    contador = 0
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if matriz[lin][col] == numero:
                contador += 1
    return contador