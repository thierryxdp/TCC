def maiores(lista, n):
    """Função que irá
    
    list, int -> list
    """
    
    nova_lista = lista [:]
    list.append(nova_lista, n)
    list.sort(nova_lista)
    index = list.index(nova_lista, n)
    return nova_lista[index+1:]