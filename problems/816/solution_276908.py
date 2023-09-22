def maiores (lista, n):
    """Função que dada uma lista e um numero inteiro n, retorna uma nova lista que contenha todos os numeros da lista original maiores que n;
       list, int -> list."""
    list.insert (lista, 0, n)
    list.sort (lista)
    lista_nova= list.index (lista, n)
    return lista [(lista_nova +1):]