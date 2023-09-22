def maiores(l, n):
    """Retorna uma nova lista contendo todos os números maiores que n da lista original.
    list, int -> list"""
    l2 = sorted(l)
    n_index = l2.find(n)
    if n <= l2[len(l2) - 1]:
        return l2
    return maiores(l2[1:], n)