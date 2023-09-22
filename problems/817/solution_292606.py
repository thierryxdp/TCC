def maiores(lista,n):
    """Retorna uma lista que contém todos os números da lista original
       maiores que n
       list, int --> list"""
	if n not in lst:
  		lista.append(n)

	lista.sort()
	r = lista[lista.index(n)+1:]
	return r

def acima_da_media(lista):
	"""Retorna uma lista ordenada com as notas que ficaram acima da média
       list --> list"""
	n = (sum(lista) / len(lista))
    lista.sort()
    maiores(lista,n)
    return r