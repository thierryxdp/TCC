def acima_da_media(lista):
    '''função que, dada uma lista com as notas dos alunos de uma turma, retorne
    uma lista ordenada com as notas acima da média; '''
    media = sum(lista)/len(lista)
    if media in lista:
        list.sort(lista)
        lista1=list.index(lista,media)
        return lista [lista1=1:]
    else:
        list.append(lista,media)
        list.sort(lista)
        lista1=lista.index(media)
        return lista[lista1+1:]