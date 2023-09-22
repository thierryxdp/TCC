def maiores(lista, n):
    """função que retorna uma lista com valores maiores que n
    list, int -> list"""
    if n not in lista:
        list.insert(lista,0,n)
    list.sort(lista)
    
    fati = list.index(lista,n)
    lista2 = lista[fati+1:]
    
    return lista2
def acima_da_media(notas):
    """função que retorna uma lista com as notas maiores do que a média
    list->list"""
    n=sum(notas)/len(notas)
    return maiores(notas,n)