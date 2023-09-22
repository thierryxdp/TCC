def acima_da_media(list):
    '''função que dada uma lista com notas dos alunos de uma turma,retorna uma lista
    ordenada com as notas que ficaram acima da media
    list->list'''
    list.sort()
    soma=sum(list)
    media=list.index(soma)
    return list[media,]