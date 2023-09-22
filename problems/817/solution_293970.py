def acima_da_media(lista):
    '''retorna uma lista com as notas dos alunos que ficaram
    acima da media;
    list->list'''
    n=len(lista)
    media=(sum(lista))/n
    list.append(lista,media)
    ind=list.index(lista,media)
    return lista[ind+1:]