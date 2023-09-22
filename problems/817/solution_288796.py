def acima_da_media(lista):
    '''dado uma lista com as notas dos alunos  de uma  turma, será retornado uma lista ordenada com as notas que ficaram acima da média; lista->lista'''
    media=sum(lista)/len(lista)
    list.sort(lista)
    list.append(lista, media)
    n=list.index(lista, media)
    return lista[n+1:]