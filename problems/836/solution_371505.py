def busca(setor, matriz):
    '''Busca os dados dos funcionários com base no setor
    list, str -> list'''
    dados = []
    for i in matriz:
        if i[2] == setor:
            list.append(dados, i)
            list.pop(i, 2)
	return dados