def maiores(lista, n):
    """Retorna uma lista com os elementos maiores que n na lista dada como entrdada.
list, int -> list"""
    list.insert(lista,0,n)
    list.sort(lista)
    p = list.index(lista,n)
    r = lista[p+1:]
    return r

def acima_da_media (lista):
    """Retorna uma lista ordenada com as notas que ficaram acima da média. list-> list"""
    s = sum(lista)
    l = len(lista)
    m = s/l
    list.insert(lista,0,m)
    list.sort(lista)
    p = list.index(lista,m)
    if m in lista:
        r = lista[p+2:]
        return r
    else:
        r = lista[p+1:]
        return r