def media_matriz(mat):
    '''Retorna a média dos números da matriz com precisão de
    exatamente duas casas decimais
    list -> float '''
    lin = len(mat)
	col = len(mat[0])
	i = 0
	soma = 0
	while i < lin:
    	soma = soma + sum(mat[i])
    	i = i + 1
    return round(soma/(lin*col),2)