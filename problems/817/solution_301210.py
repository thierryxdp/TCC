def maiores(L, n):
    '''Retorna uma lista com os valores de L maiores que n
    	list, int -> list'''
    list.append(L, n)
    list. sort(L)
    ind = list.index(L, n)
    return L[ind+1:]

def acima_da_media(notas):
    media = sum(notas)/len(notas)
    return maiores(notas, media)