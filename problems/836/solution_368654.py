def busca(setor,matriz):
	sectorcheck = lambda funcionario: funcionario[2]==setor
	filtrados=list(filter(sectorcheck,matriz))
	funcionariofiltrado= lambda funcionario: funcionario.remove(funcionario[2])
	return(list(map(funcionariofiltrado,filtrados)))