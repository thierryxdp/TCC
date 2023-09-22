def acima_da_media(lista):
    '''função que, dada uma lista, retorna outra lista ordenada com os elementos que ficaram 
    acima da média
    list -> list'''
    soma = sum(lista)
    media = (soma)/len(lista)
    lista = lista + [media]
    list.sort(lista)
    i = lista.index(media)
    lista = lista[i:]
    list.remove(lista,media)
    if media == lista[0]:
        return []
    else:
        return lista