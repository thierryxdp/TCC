def maiores(lista,n):\
    """funcao que dado uma lista e um numero inteiro retorna outra lista com todos os numeros inteiros maiores que n"""
	"""list,int->list"""
    if n not in lista:
        list.append(lista,n)
    list.sort(lista)
    ind = list.index(lista,n)
    listaf = lista[ind+1:]
    return listaf