def conta_numero(numero, matriz):
	#conta e retorna quantas vezes aquele um determinado número aparece na matriz
	#entrada: numero , matriz: matriz ; saida: res
    res = 0
    for i in range(0, len(matriz)):
        for o in range(0, len(matriz[i])):
            if matriz[i][o] == numero:
                res += 1

    return res