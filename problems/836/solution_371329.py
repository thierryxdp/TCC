def busca(Procurar, Matriz):
    lista = []
    for linha in Matriz:
        if Procurar in linha:
            for coluna in linha:
                if coluna != Procurar:
                    lista += coluna
	return lista