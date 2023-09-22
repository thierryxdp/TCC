def media_matriz(matriz):
    '''função que dada uma matriz de inteiros não vazia, retorna a 
    média de todos os números da matriz;
    lista-->float'''
    
	nlinha=len(matriz)
	ncoluna=len(matriz[0])
	soma=0
	media=soma/(nlinha*ncoluna)
    
	for linha in range(nlinha):
		for coluna in range(ncoluna):
			soma=soma+int(matriz[linha][coluna])

	return round(media,2)