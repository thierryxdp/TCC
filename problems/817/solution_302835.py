def maiores(lista, n):
    '''Função retorna os números maiores do que um determinado número em ordem crescente
       list int --> list'''
    lista.append(n)
    lista.sort()
    i = lista.index(n)
    return lista[i+1::]

def acima_da_media(lista):
	'''Função retorna as notas acima de uma certa média
       list --> list'''
    media = sum(lista)/len(lista)
    l = maiores(lista, media)
    if len(l) == 1 and l == lista[0:1:]:
        return []
    return l