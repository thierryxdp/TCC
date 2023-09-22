def maiores(l, n):
    """Retorna uma nova lista contendo todos os números maiores que n da lista original.
    list, int -> list"""
    l2 = sorted(l)
    if n >= l2[0]:
    	return maiores(l2[1:], n)
    return l2