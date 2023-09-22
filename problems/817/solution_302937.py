def acima_da_media(notas):
    '''funçao que recebe uma lista com as notas dos alunos de uma turma e retorna uma lista
    ordenada com as notas que ficaram acima da media
    list-->list'''
    a=sum(notas)/len(notas)
    list.append (notas,a)
    list.sort(notas)
    b=list.index(notas,a)
    if len(notas)==3:
        return[]
    else:
        return notas[b+1:]