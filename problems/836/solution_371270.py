def busca(Procurar, matriz): 
    lista = []
    for linha in matriz:
        for coluna in linha:
            if coluna == Procurar:
                linha.remove(Procurar)
                lista += [linha]
	if Procurar not in matriz[0]:
        return []
	return lista