def acima_da_media(lista):
    '''Função que recebe uma lista com notas dos alunos e
    retorna uma lista ordenada com as notas que ficaram 
    acima da média; list -> list'''
    media = sum(lista)/len(lista)
    if media in lista and list.count(lista, media) < 2:
        list.sort(lista)
        return lista[list.index(lista, media):]
    elif media in lista and list.count(lista, media) >= 2:
        list.sort(lista)
        return lista[list.index(lista, media)+list.count(lista, media)-1:]
    else:
        list.append(lista, media)
        list.sort(lista)
        return lista[list.index(lista, media)+1:]