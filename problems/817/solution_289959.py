def media(lista):
    '''Funcao que calcula a media da nota dos alunos de uma sala,
    a partir de uma lista dada
    list->int'''
    if 0 in lista:
        return sum(lista)//(len(lista)-1)
    else:
        return sum(lista)//len(lista)
def acima_da_media(lista):
    ''' Funcao que retorna a lista das notas dos alunos a cima da media da sala.
    list->list'''
    L=lista
    list.insert(L,0,media(lista))
    L.sort()
    K=list.index(L,media(lista))
    if media(lista) in lista:
        return L[K+1: ]
    else:
        return L[K+1: ]