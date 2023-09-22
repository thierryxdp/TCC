def busca(setor,matriz):
    funcionarios = []
    for i in matriz:
        dados = []
        if setor in i:
            dados.append(i[0],i[1],i[3])
            funcionarios.append(dados)
	return funcionarios