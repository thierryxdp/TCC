def maiores(L, n):
    '''Retorna uma lista com os valores de L maiores que n
    	list, int -> list'''
    list.append(L, n)
    list. sort(L)
    ind = list.index(L, n)
    return L[ind+1:]

def acima_da_media(notas):
    '''Retorna as notas acima da média
    	list -> list'''
    media = sum(notas)/len(notas)
    list.sort(notas)
    lista = maiores(notas, media)
    if lista[0] == media:
        del lista[0]
    return lista