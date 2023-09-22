def acima_da_media(lista):
    '''Calcula a media da turma e retona as notas acima da media. list ->list'''
    media = sum(lista)//len(lista) 
    if media in lista:
        lista1 = sorted(lista)
        indice = lista.index(media)
        return lista1[indice+2:]
    lista.append(media)
    lista1 = sorted(lista)
    indice = lista1.index(media)
    return lista1[indice+1:]