def maiores(lista_numeros):
    	"""funcao que retorna uma lista que contem os valores maiores que um determinado numero n"""
    copiaLista=lista_numeros[:4:]
    copiaLista.sort()
    	return copiaLista[+1]