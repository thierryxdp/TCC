def media_matriz (matriz):
    """Função que, dada uma matriz, retorna a média de todos os números da matriz
    Entrada: list.
    Saída: int."""
    

	S = [0]*len(Matriz)
	for i in range(0,len(Matriz)):
		soma_linhas = 0
		for j in range(0,len(Matriz[0])):
			soma_linhas += Matriz[i][j]
		S[i] = soma_linhas
	return S