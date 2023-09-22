def busca(setor,matriz):
	def sector(funcionario):
		return(funcionario[2]==setor)
	return(list(filter(sector,matriz)))