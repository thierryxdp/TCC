def busca(Procurar, matriz): 
    lista = []
    if Procurar not in matriz[0]:
        return []
    for linha in matriz:
        for coluna in linha:
            if coluna == Procurar:
                lista += linha
	return lista