def acima_da_media(lista):
    '''função que dada uma lista com notas, retorna uma lista ordenada que inclui
       somente as notas acima da média. list -> list'''
    media = sum(lista) / len(lista)
    list.append(lista,media)
    list.sort(lista)
    indice = list.index(lista,media)
    lista = lista[:indice:-1]
    list.reverse(lista)
    if (media in lista):
        list.remove(lista,media)
    else:
        lista = lista
    return lista