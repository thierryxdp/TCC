def maiores(lista, n):
    '''Função que dada uma lista de números e um inteiro n, retorna uma lista ordenada contendo os números da lista original maiores que n.
    list, int -> list'''
    list.append(lista,n)
	list.sort(lista)
    return lista[list.index(lista,n)+1:]
def acima_da_media(lista):
    '''Função que dada uma lista com notas, retorna outra lista apenas com as maiores que a media da primeira lista. list ->list'''
    media= sum(lista)/len(lista)
	return maiores(lista,media)