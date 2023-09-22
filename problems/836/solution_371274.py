def busca(Procurar, matriz):
    lista = []
	for linha in matriz:
        if Procurar in linha:
            linha.remove(Procurar)
          	lista = [linha]
            return lista