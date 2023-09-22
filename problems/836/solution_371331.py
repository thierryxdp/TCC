def busca(Procurar, Matriz):
    lista = []
    for linha in Matriz:
        if Procurar in linha:
        	lista += [linha]
	return lista