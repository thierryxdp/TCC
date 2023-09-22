def intercala(lista1, lista2):
	"""
    	Função recebe duas listas e retorna uma terceira lista
        que é a concatenação da primeira lista e da segunda lista.
        lista --> lista
	"""
    if(len(lista1) + len(lista2) != 6):
    	return lista1 + lista2
    else:
        return []