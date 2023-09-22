def maiores(lista, n):
    """Retorna todos os números da lista maiores que n em
    uma nova lista;
    list, int -> list"""
    list.append(lista, n)
    list.sort(lista)
    lista = lista[list.index(lista,n):]
    list.remove(lista,n)
    
    return lista