def crie_matriz(n_linhas, n_colunas, valor):
    ''' (int, int, valor) -> matriz (lista de listas) - Cria e retorna uma matriz com n_linhas linha e n_colunas em que cada elemento é igual ao valor dado.'''
    matriz = [] # lista vazia
    for i in range(n_linhas):
        linha = [] # lista vazia
        for j in range(n_colunas):
            linha += [valor]
           
        matriz += [linha]
	return matriz