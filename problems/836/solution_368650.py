def busca(setor,matriz):
	def sector(setor,funcionario):
		return(funcionario[2]==setor)
	return(list(filter(sector,matriz)))