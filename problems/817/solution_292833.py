def acima_da_media(notas):
    '''Dado uma lista com as notas dos alunos, retorna os alunos acima da media
    da turma;
    list-> list'''
    media=sum(notas)/len(notas)
    list.sort (notas)
    x=list.index(notas,round(media))
    return notas[x:]