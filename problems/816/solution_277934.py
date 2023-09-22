def maiores(x,n):
    """função que retorna de uma lista original, outra lista com números maiores que um dado número n
    list, int -> list"""
    x += [n]
    list.sort (x)
    a = list.index(x,n)
    b = x[a+1:]
    return b