def busca (setor, lista):
    lista2 = []
    for a in range(len(lista)):
        if lista[a][2] == setor:
            del lista[a][2]
            lista2 = lista[a]
    	return lista2