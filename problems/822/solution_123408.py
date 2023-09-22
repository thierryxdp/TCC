def repetidos(listadenumeros):
	sequenciais=list(zip(listadenumeros,listadenumeros[1:]))
	def tuplasiguais(x):
		return(x[0]==x[1])
	repetidos=list(filter(tuplasiguais,sequenciais))
	return(len(repetidos))