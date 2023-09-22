def maiores(lista:list, n:int) ->list:
    """Recebe uma lista e um numero e retorna uma outra lista que contenha apenas
    	maiores que o número indicado."""
    list.append(lista, n)
    list.sort(lista)
    return lista[list.index(lista,n)+1:]