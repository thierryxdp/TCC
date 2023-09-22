def maiores (lista, n):
    """retorna uma lista com todos os números maiores que n em ordem crescente; lista, int -> lista"""
    if n in lista:
    l1= list.index((list.sort(lista)), n)
    return lista[l1+1]
	else:
        list.insert(lista,n)
        list.sort(lista)
        l2=list.index(lista,n)
        return lista[lista+1:]