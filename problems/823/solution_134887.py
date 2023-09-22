def faltante(pecas):
	list.sort(pecas)
	i=0
	while pecas[i]==pecas[i+1]-1:
		i+=1
	return pecas[i]+1