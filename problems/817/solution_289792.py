def media(lista):
    '''Funcao que calcula a media da nota dos alunos de uma sala,
    a partir de uma lista dada
    list->int'''
    f=sum(lista)//len(lista)
    return f
def acima_da_media(lista):
    ''' Funcao que retorna a lista das notas dos alunos a cima da media da sala.
    list->list'''
    L=lista
    list.insert(L,0,media(lista))
    L.sort()
    K=list.index(L,media(lista)) 
    return L[K+1: ]