def maiores (lista,n):
    list.append(lista,n)
    list.sort(lista)
    p = list.index(lista,n)
    x = lista[p:]
    del x[0]
    return x

def acima_da_media(lista):
    '''Esta função retorna uma lista com as notas maiores que
    a média, dada uma lista de notas inicial.
    list -> list'''
    media = int(sum(lista))/int(list.count(lista))
    x = maiores(lista,media)
    return x