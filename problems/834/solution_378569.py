def media_matriz(m):
	soma = 0
	for i in range(len(m)):
		for j in range(len(m[0])):
			soma += m[i][j]
	return round(soma/(len(m) * len(m[0])), 2)