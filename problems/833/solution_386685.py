def conta_numero(numero, matriz):
    """
    	Retorna a quantidade de vezes que um número aparece na matriz.
        int, list -> int
    """
    vezes=0
    for i in range(len(matriz)):
        for j in range (len(matriz[0])):
            if matriz[i][j] == numero:
                vezes += 1
    return vezes