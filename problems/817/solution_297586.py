def acima_da_media(lista_nota):
    '''Recebe uma lista com notas de alunos, calcula a media das
notas e retorna as notas que estão iguais ou acima da media.
list --> list'''
    lista = lista_nota[:]
    media = sum(lista_nota)//len(lista_nota)
    if media in lista:
        list.sort(lista)
        return lista[int(list.index(lista,media)+1):]
    else:
        list.append(lista,media)
        list.sort(lista)
        return lista[int(list.index(lista,media)+1):]