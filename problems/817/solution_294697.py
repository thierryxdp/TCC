def acima_da_media(lista):
    ''' Função que faz a media das notas e retorna uma lista só com quem ficou acima desta média
    list -> list'''
    n = sum(lista) / len(lista)
    lista.append(n)
    list.sort(lista)
    list.reverse(lista)
    a = list.index(lista, n)
    del lista[a:]
    list.reverse(lista)

    return lista