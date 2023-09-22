def busca(elemento, matriz):
    '''Dada uma matriz como o exemplo citado e um
    nome a ser buscado, retorna os dados de todos
    os funcionarios daquele setor
    list -> list'''
    lista = []
    n = 0
    for linha in matriz:
        if linha[2] == elemento:
            lista.append(linha)
        	del lista[n][2]
            n += 1
	return lista