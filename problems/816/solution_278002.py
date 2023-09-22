def maiores (*n):
    """essa funcao retorna uma lista com todos os elementos
	 maiores que o numero inteiro n"""
    
    lista_n = n[0]
    x = n[1]
    lista_n.append(x)
    
    if max(lista_n) == x:
        return []
   
	else:
        lista1 = sorted(lista_n, reverse = True)
        n_index = lista1.index(x)
        return sorted(lista1[:n_index])