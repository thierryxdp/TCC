def maiores(lista,n):
    """Dada uma lista de numeros e o numero n, retorna todos os numeros
    da lista original que sejam maiores que n.
    Entradas:
    	lista -> lista
        n -> int
    Returns: lista"""
    lista2 = lista + [n]
    list.sort(lista2)
    i = list.index(lista2,n)
    return lista2[(i+1):]