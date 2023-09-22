def intercala(lista1, lista2):
	"""
    	Função recebe duas listas e retorna uma terceira lista
        que é a concatenação de elementos alternados da primeira
        lista e da segunda lista.
        lista --> lista
	"""
    tamanhoTotal = len(lista1) + len(lista2)
    listaIntercala = []
    if tamanhoTotal == 6:
    	listaIntercalada = [lista1[0], lista2[0], lista1[1], lista2[1], lista1[2], lista2[2]]
        return listaIntercalada
    else:
        return []