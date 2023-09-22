def conta_numero(numero, matriz):
   # Função que dado um número e uma matriz, verifica quantas vezes aquele numero esteve na matriz
	# int, list -> int
    indice = 0
    matrizNum = 0
    for i in range(len(matriz)):
        for counter in range(len(matriz[i])):
            if matriz[i][counter] == matrizNum:
                indice += 1
    return indice