def maiores(lista,n):
    """A função retorna outra lista que contenha todos os números da 
    lista original maiores que n, ordenados em ordem crescente.
    list--int-->list."""
    
    if n in lista:
        list.sort(lista)
        nova_lista = lista[list.index(lista,n)+1:]
        return nova_lista
    
    else:
        lista.insert(0,n)
        list.sort(lista)
        nova_lista = lista[list.index(lista, n)+1:]
        return nova_lista

def acima_da_media(lista):
    """A função retorna uma lista ordenada com as notas que
    ficaram acima da média.
    list-->list."""
    media = int(sum(lista)/len(lista))
    return maiores(lista, media)