def media_matriz(matriz):
    '''função que dada uma matriz de inteiros não vazia, retorna a
    média de todos os números da matriz com precisão de duas casas
    decimais; lista-->float'''
    
	nlinha=len(matriz)
	ncoluna=len(matriz[0])
	soma=0
	qtd=nlinha*ncoluna
    
	for linha in range(nlinha):
		for coluna in range(ncoluna):
			soma=soma+int(matriz[linha][coluna])
            
	media=soma/qtd
    
	return round(media,2)