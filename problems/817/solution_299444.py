def acima_da_media(lista):
    '''Calcula a media da turma e retona as notas acima da media. list ->list'''
    media = sum(lista)//len(lista)
    lista.append(media)
    lista1 = sorted(lista)
    indice = lista1.index(media)
    del (lista1[0:indice+1])
    return lista1