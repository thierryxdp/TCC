def conta_numero(numero, matriz):
   # Função que dado um número e uma matriz, verifica quantas vezes aquele numero esteve na matriz
	# int, list -> int
    indice = 0
    for i in range(0, len(matriz)):
        for counter in range(0, len(matriz[i])):
            if matrizInt[i][counter] == matrizNum:
                indice += 1
    return indice