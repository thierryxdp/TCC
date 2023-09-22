def faltante(peças):
	list.sort(peças)
	i=0
	while peças[i]==peças[i+1]-1:
		i+=1
	return peças[i]+1