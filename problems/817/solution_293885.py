def acima_da_media(l):
    '''Dado uma lista com a nota dos alunos, retorna uma lista
    ordenada com as notas acima da media entre elas. list->list'''
    media = sum(l)//len(l)+1
    l = l+[media]
    list.sort(l)
    x=list.index(l,media)
    l[0:x+1]=[]
    return l