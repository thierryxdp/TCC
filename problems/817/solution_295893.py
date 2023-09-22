def acima_da_media(lista):
    '''função que retorna uma lista com as notas dos alunos acima da media a partir de uma lista como dado de entrada com as notas dos alunos;list->list'''
    media=(sum(lista))/(len(lista))
    lista=lista+[media]
    list.sort(lista)
    del lista[:(list.index(lista,media))]
    del lista[0]
    if media in lista:
        return lista[1:]
    else:
        return lista