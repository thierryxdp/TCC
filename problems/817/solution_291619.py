def maiores(lista_numero, n):
    '''Retorna uma lista com todos os números maiores que n.
    list, int -> list'''
    lista = lista_numero+[n]
    list.sort (lista)
    pos = list.index(lista,n)
    return lista[pos:]

def acima_da_media(lista):
	'''Retorna as notas iguais e acima da média.
	list -> list'''
    media = sum(lista)/len(lista)
    return maiores(lista, media)