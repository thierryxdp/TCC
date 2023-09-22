def busca(Procurar, matriz):
    lista = []
	for linha in matriz:
        if Procurar in linha:
          	lista = [linha]
            lista.remove(Procurar)
            return lista