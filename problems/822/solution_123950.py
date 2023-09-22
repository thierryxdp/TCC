def repetidos(lista):
    """função que recebe uma lista de números como entrada e retorna o número de vezes
	que um elemento da lista é igual ao elemento anterior
	list -> int"""
    
    j = 1
    cont = 0
    
    while j < len(lista):
        if lista[j] == (lista[j-1]):
            cont += 1
        j += 1
        
	return cont