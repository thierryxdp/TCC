def maiores(lista,n):
    """A função retorna outra lista que contenha todos os números da 
    lista original maiores que n, ordenados em ordem crescente.
    list--int-->list."""
    
    if n in lista:
        list.sort(lista)
        nova_lista = lista[list.index(lista,n)+1:]
        return nova_lista
    
    else:
        list.insert(0,n)
        list.sort(lista)
        nova_lista = lista[list.index(lista, n)+1:]
        return nova_lista