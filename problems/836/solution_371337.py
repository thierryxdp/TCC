def busca(Procurar, Matriz):
    lista = []
    lista2 = []
    for linha in Matriz:
        if Procurar in linha:
        	lista += [linha]
            for linha2 in lista:
                linha2.remove(Procurar)
                lista2 += [linha2]
    	return lista2