def busca(Procurar, matriz): 
    lista = []
    for linha in matriz:
        if Procurar not in linha:
            return []
        for coluna in linha:
            if coluna == Procurar:
                linha.remove(Procurar)
                lista += [linha]
	
	return lista