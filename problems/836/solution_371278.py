def busca(Procurar, matriz):
    lista = []
	for linha in matriz:
        if Procurar in linha:
        	for coluna in linha:
                if coluna != Procurar
                	lista += [coluna]
            return lista