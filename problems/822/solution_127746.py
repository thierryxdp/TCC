def repetidos(lista):
    """ A funçaõ retorna o número de vezes que um elemtento da lista aparece
    	list -> int """
    
    i = 0
    a = 0
    while i < len(lista):
		if lista[i] == lista[i-1]:
        	x = x + 1
		i = i + 1
	return x