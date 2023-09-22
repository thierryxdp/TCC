def busca(setor, matriz):
    funcionarios = []
    for linha in matriz:
        for string in linha:
        	if string == setor:
                dados = list.remove(linha, setor)
            	list.append(funcionarios, dados)
    return funcionarios