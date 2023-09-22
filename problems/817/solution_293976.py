def acima_da_media(lista):
    '''retorna uma lista com as notas dos alunos que ficaram
    acima da media;
    list->list'''
    n=len(lista)
    media=(sum(lista))/n
    if media in lista:
        list.append(lista,media)
        list.sort(lista)
        ind=list.index(lista,media)
        return lista[ind+2:]
    else:
        list.append(lista,media)
        list.sort(lista)
        ind=list.index(lista,media)
        return lista[ind+1:]