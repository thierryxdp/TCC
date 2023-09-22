def media_matriz(matrix):
	'''retorna a média da somaada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz (com exatamente duas casas decimais de precisão);list(list)->float'''
    lil_Li=0
    peso_pesado=len(matrix[0])*len(matrix)
    for j in matrix:
        for i in j:
        	lil_Li+=i
    return round(lil_Li/peso_pesado,2)