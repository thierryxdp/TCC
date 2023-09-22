def  acima_da_media(lista):
    '''funçao que dada uma lista com as notas dos alunos,
    retorna a lista ordenada e apenas com as notas acima da media;
    list->list'''
    media=sum(lista)/len(lista)
    list.append(lista, media)
    list.sort(lista)
    media_e_acima=lista[list.index(lista,media)+1:]
    if media not in media_e_acima:
        return media_e_acima
    else:
        list.remove(media_e_acima, media)
        return media_e_acima