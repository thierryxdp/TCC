def maiores(lista,n):
    """
    	Retorna uma lista com os elementos da lista original que são maiores que n
    	list,int -> list
    """
    if not(n in lista):
        list.append(lista,n)
    	list.sort(lista)
    return lista[list.index(lista,n)+1:]