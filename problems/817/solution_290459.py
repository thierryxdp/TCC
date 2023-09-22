def acima_da_media(lista):
    '''funcao que dado uma lista com as notas dos alunos de uma turma, retorna uma lista com os aprovados
    list->list'''
    x=lista
    y=(sum(x))/len(x)
    x.append(y)
    list.sort(x)
    w=x.index(y)
    z=len(x)
    return x[y+1:z]