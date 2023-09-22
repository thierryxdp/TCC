def busca(elemento, matriz):
    '''Dada uma matriz como o exemplo citado e um
    nome a ser buscado, retorna os dados de todos
    os funcionarios daquele setor
    list -> list'''
    lista = []
    for linha in matriz:
        if linha[2] == elemento:
            lista.append(linha[0])
            lista.append(linha[1])
            lista.append(linha[3])
	return lista