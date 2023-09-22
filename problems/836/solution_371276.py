def busca(Procurar, matriz):
    lista = []
	for linha in matriz:
        if Procurar in linha:
         	for coluna in linha:
                linha.remove(Procurar)
                lista += [linha]