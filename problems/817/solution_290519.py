def acima_da_media(lista):
    '''Dado uma lista com as notas dos alunos, retorne uma nova lista ordenada com valores acima da média;
    list -> list'''
    media=sum(lista)/len(lista)
    if media in lista:
        list.sort(lista)
        a=list.index(lista,media)
        return lista[a+1:]
    list.append(lista,media)
    list.sort(lista)
    b=list.index(lista,media)
    return lista[b+1:]