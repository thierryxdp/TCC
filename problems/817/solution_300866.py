def maiores(lista, n):
    """Esta funcao recebe uma lista com numeros inteiros, um numero n, e
    retorna outra lista que contem somente os numeros maiores que n da lista
    original."""
    list.append(lista, n)
    list.sort(lista)
    if len(lista)>2:
        return lista[list.index(lista, n)+1:]
    else:
        return []
    
def acima_da_media(notas):
    """"""
    media=sum(notas)/len(notas)
    return maiores(notas, media)