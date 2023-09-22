def conta_numero(numero, matriz):
    """Função que conta quantas vezes um dado numero aparece em uma matriz
    int,list-> int"""
    cont = 0
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if matriz[i][j] == numero:
                cont += 1
    return cont