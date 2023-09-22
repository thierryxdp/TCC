def maiores(lst,n):
    """Retorna uma lista que contém todos os números da lista original
       maiores que n
       list, int --> list"""
	if n not in lst:
  		lst.append(n)

	lst.sort()
	r = lst[lst.index(n)+1:]
	return r

def acima_da_media(lista):
	"""Retorna uma lista ordenada com as notas que ficaram acima da média
       list --> list"""
    n = media
	media = (sum(lista) / len(lista))
    lista.sort()
    maiores(lst,n)
    return r