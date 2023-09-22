def busca(setor,matriz):
    funcionarios = []
    for i in matriz:
        if setor in i:
            funcionarios.append(i)
	return funcionarios