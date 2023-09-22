def busca(Procurar, matriz): 
    lista = []
    if Procurar not in matriz[0]:
        return []
    for linha in matriz:
        for coluna in linha:
            if coluna == Procurar:
                linha.remove(Procurar)
                lista += [linha]
	return lista