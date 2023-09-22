def acima_da_media(notas):
    '''Recebe uma lista de notas dos alunos e retorna aquelas que foram acima da media; list->list'''
    media=sum(notas)/len(notas)
    list.sort(notas)
    return notas[math.ceil(media):]