def filtraMultiplos(listadenumeros,numero):
	def multiplos(numero1,numero):
		return(numero1%numero==0)
	return(list(filter(multiplos,listadenumeros,numero)))