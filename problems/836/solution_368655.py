def busca(setor,matriz):
	sectorcheck = lambda funcionario: funcionario[2]==setor
	filtrados=list(filter(sectorcheck,matriz))
	def funcionariofiltrado(funcionario):
		funcionario.pop(2)
		return(funcionario)
	return(list(map(funcionariofiltrado,filtrados)))