def media_matriz(mat):
    ''''''
    lin = len(mat)
	col = len(mat[0])
	i = 0
	soma = 0
	while i < lin:
    	soma = soma + sum(mat[i])
    	i = i + 1
    	return soma/lin