def busca(setor,matriz):
    funcionarios = []
    for i in matriz:
        dados = []
        if setor in i:
            dados.append(i[0])
            dados.append(i[1])
            dados.append(i[3])
            funcionarios.append(dados)
	return funcionarios