# Função que dadas duas listas (lista1 e lista2) de tamanho 3, gera uma lista L3 que  ́e formada intercalando os elementos da lista1 e da lista2.
# lista1, lista2
def intercala(lista1, lista2):
    """Função que dadas duas listas (lista1 e lista2) de tamanho 3, gera uma lista L3 que  ́e formada intercalando os elementos da lista1 e da lista2.
    
    	Parameters:
        lista1: lista de tamanho 3
        lista2: lista de tamanho 3
    
    	Returns:
        lista com os valores de lista1 e lista2 intercalados    
	"""
    
    return [lista1[0]] + [lista2[0]] + [lista1[1]] + [lista2[1]] + [lista1[2]] + [lista2[2]]