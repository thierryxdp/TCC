def acima_da_media(notas):
    '''procura a media na turma e retorna todos que tiraram acima da media
    list->list'''
    media=sum(notas)/len(notas)
    acima_da_media=[]
    for c in notas:
        if c>media:
            acima_da_media.append(c)
    return sorted(acima_da_media)