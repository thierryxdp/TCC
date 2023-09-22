def maiores(lista, n):
    """Retorna uma lista contendo todos os números da lista de entradas maiores que n; lista, int -> lista."""
    if list.count(lista,n)==0:
        list.append(lista,n)
        list.sort(lista)
        list.reverse(lista)
        novalista = lista[:list.index(lista,n)]
        list.sort(novalista)
        return novalista
    else:
        list.sort(lista)
        list.reverse(lista)
        novalista2 = lista[:list.index(lista,n)]
        list.sort(novalista2)
        return novalista2
    
def acima_da_media(lista):
    """Retorna uma lista com as notas acima da média; lista -> lista."""
    n = sum(lista)/2
    x = maiores(lista,n)
    return x