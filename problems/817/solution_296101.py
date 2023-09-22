def acima_da_media(notas):
    '''Recebe uma lista de notas dos alunos e retorna uma nova lista com aquelas que foram acima da media; list->list'''
    media=sum(notas)/len(notas)
    list.append(notas,media)
    list.sort(notas)   
    return notas[list.index(notas,media)+1:]