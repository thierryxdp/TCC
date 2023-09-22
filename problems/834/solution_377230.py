def media_matriz (matriz):
    """Função que, dada uma matriz, retorna a média de todos os números da matriz
    Entrada: list.
    Saída: int."""
    

	
    soma_linhas = 0
	for linha in matriz:
		for coluna in linha:
			soma_linhas += coluna
		
	media = (soma_linhas)/(len(matriz)*len(matriz[0]))
    
    return round(media,2)