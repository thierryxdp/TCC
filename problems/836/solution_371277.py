def busca(Procurar, matriz):
    lista = []
	for linha in matriz:
        if Procurar in linha:
        	for coluna in linha:
                lista += [coluna]
                lista.remove(Procurar)
                return lista