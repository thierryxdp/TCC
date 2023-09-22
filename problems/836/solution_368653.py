def busca(setor,matriz):
	def sector(funcionario):
		return(funcionario[2]==setor)
	filtrados=list(filter(sector,matriz))
	funcionariofiltrado=lambda funcionario: del(funcionario[2])
	return(list(map(funcionariofiltrado,filtrados)))