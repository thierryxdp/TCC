def filtraMultiplos(numeros,n):
	"""filtra a lista de numeros(numeros) retorna lista com apenas
os numeros disiveis por n; list[float],float->list[float]"""
	i=0
	mult=[]
	while i<len(numeros):
		if numeros[i]%n==0:
			mult.append(numeros[i])
		i+=1
	return mult