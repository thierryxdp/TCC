def repetidos(numeros):
	i=1
	rept=0
	while i<len(numeros):
		if numeros[i]==numeros[i-1]:
			rept+=1
		i+=1
	return rept