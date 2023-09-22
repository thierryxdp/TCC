def maiores(lst,n):
    """Retorna uma lista que contém todos os números da lista original
       maiores que n
       list, int --> list"""
	if n not in lst:
  		lst.append(n)

	lst.sort()
	r = lst[lst.index(n)+1:]
	return r