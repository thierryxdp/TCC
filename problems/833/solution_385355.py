def conta_numero(numero,matriz):
    """Retorna a quantidade de vezes que o numero aparece na matriz;
    	int,list -> int"""
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                total = total + 1
    return total