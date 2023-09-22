def acima_da_media(notas):
    '''Esta funcao calcula as notas que ficaram acima da media de uma turma.'''
    '''list --> list'''
    if len(notas) > 1:
        media = sum(notas)/len(notas)
        list.append(notas, media)
        list.sort(notas)
        indice = list.index(notas, media)
        acima_da_media = notas[(indice + 1):]
        return acima_da_media
    else:
        return notas