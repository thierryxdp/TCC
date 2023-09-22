def media_matriz(Matrix):
	def mean(numeros):
		return(sum(numeros)/(len(Matrix)*len(Matrix[0])))
	meanmatrix=sum(map(mean,Matrix))
	return(round(meanmatrix,2))