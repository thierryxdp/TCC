def maiores(lista,n):
    """retorna uma lista, que contem todos os numeros de 'lista' maiores que n.
    list,int->list"""
    list.append(lista,n)
    list.sort(lista)
    x=list.index(lista,n)
    del lista[:x+1]
    return lista