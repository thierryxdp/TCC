def conta_numero(numero,matriz):
    """A funcao conta a quantidade de vezes que o numero de entrada parece na matriz tambem de entrada
    .int,list(matriz)-->int"""
    conta = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                conta = conta + 1
    return conta