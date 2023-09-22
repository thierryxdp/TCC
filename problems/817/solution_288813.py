def acima_da_media(lista):
    '''dado uma lista com as notas dos alunos  de uma  turma, será retornado uma lista ordenada com as notas que ficaram acima da média; lista->lista'''
    media=sum(lista)/len(lista)
    if media in lista:
        list.sort(lista)
        n = list.index(lista, media)
        return lista[n+1:]
    elif media not in lista:
        media=sum(lista)/len(lista)
    	list.append(lista,media)
    	list.sort(lista)
        n=list.index(lista, media)
        return lista[n:]