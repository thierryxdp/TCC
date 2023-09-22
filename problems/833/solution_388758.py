def conta_numero(numero,matriz):
    """Essa funcao recebe uma matriz e conta o numero de ocorrências do numero na matriz
    int , list -> int"""
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                contador += 1
    return contador