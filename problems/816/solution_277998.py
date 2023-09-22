def maiores (*n):
    """essa funcao retorna uma lista com todos os elementos
	 maiores que o numero inteiro n"""
    
    lista_n = n[0]
    a = n[1]
    lista_n.append(a)
    if max(lista_n) == a:
        return []
    else:
        lista1 = sorted(lista_n, reverse = true)
        n_in = lista1.index(a)
        return sorted(lista1[:n_in])