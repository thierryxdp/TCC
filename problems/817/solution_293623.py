def acima_da_media(list):
    '''função que dada uma lista com notas dos alunos de uma turma,retorna uma lista
    ordenada com as notas que ficaram acima da media
    list->list'''
    media=sum(list)//len(list)
    list.append(media)
    list.sort()
    pos_media=list.index(media)
    return list[pos_media+1:]