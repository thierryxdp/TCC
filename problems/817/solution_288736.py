def acima_da_media(lista_notas):
    '''retorna uma lista com as notas acima da media
    list->list'''
    media=sum(lista_notas)//len(lista_notas)
    list.append(lista_notas,media)
    list.sort(lista_notas)
    return lista_notas[list.index(lista_notas,media)+1:]