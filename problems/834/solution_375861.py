def media_matriz (matriz):
    """Função que, dada uma matriz, retorna a média de todos os números da matriz
    Entrada: list.
    Saída: int."""
    

	S = [0]*len(matriz)
	for i in range(0,len(matriz)):
		soma_linhas = 0
		for j in range(0,len(matriz[0])):
			soma_linhas += matriz[i][j]
		S[i] = soma_linhas
        
	return round(sum(S)/(len(matriz[0])*len(matriz)),2)