def media_matriz (matriz):
    """Função que, dada uma matriz, retorna a média de todos os números da matriz
    Entrada: list.
    Saída: int."""
    

	S = [0]*len(matriz)
    
	for linha in matriz:
		soma_linhas = 0
		for coluna in linha:
			soma_linhas += coluna
		S[coluna] = soma_linhas
	
    media = sum(S)/((len(matriz[0])*len(matriz))
    resultado = round(media,2)
        
	return resultado