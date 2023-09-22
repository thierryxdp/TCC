def media_matriz(m):
	c = 0
	for i in range(len(m)):
		for j in range(len(m[0])):
			c += m[i][j]
	return round(c / (len(m) * len(m[0])), 2)