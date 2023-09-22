def maiores(lista_int,n):
    """Retorna uma lista que contém todos os números da lista original
       maiores que n
       list, int --> list"""
    n = 0
	lst = [1,2,3,4,5,6]
	if n not in lst:
  		lst.append(n)

		lst.sort()
		r = lst[lst.index(n)+1:]
	print(r)