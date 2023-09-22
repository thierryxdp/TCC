def acima_da_media(lista):
    '''Recebe uma lista de notas e devolve uma lista com todos
    os valores maiores q a media e ordenados'''
    j= sum(lista)
    i= len(lista)
    m= j/i
    list.append(lista, m)
    list.sort(lista, reverse=True)
    pos=list.index(lista,m)
    del lista_n[pos:]
    list.sort(lista)
    return lista