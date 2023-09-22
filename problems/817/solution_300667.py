def maiores(lista, n):
    '''Dada uma lista e um numero 'n', retorna
    uma outra lista contendo todos os numeros da lista
    original maiores que 'n';
    lista, int -> lista'''
    lista.append(n)
    lista.sort()
    return lista[lista.index(n) + 1:]

def acima_da_media(lista):
	'''Dada uma lista, retorna uma lista ordenadas
    com os valores acima da media;
    list -> list'''
    return maiores(lista, sum(lista)/len(lista))