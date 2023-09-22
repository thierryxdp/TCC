def insere(lista,n):
    """funcao que dada uma lista ordenada de numeros inteiros e um numero n, inclui n na posicao certa de forma que continue ordenada"""
	"""list,int->list"""
    
    list.append(lista,n)
    lista = list.sort(lista)
    
    return lista