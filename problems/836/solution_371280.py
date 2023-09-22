def busca(Procurar, matriz):
    lista = []
    for linha in matriz:
        if Procurar in matriz:
        	for coluna in linha:
            	if Procurar not in coluna:
                	lista += [coluna]
        	return lista