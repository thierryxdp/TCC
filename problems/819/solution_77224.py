def filtraMultiplos(listadenumeros,numero):
	def multiplos(numero1,numero2):
		return(numero1%numero2==0)
	return(list(filter(multiplos,listadenumeros)))