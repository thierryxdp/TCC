def maiores(l, n):
    """Retorna uma nova lista contendo todos os números maiores que n da lista original.
    list, int -> list"""
    l2 = [x for x in l if x > n]
    return sorted(l2)