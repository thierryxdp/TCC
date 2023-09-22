def acima_da_media(lista):
    '''funcao que dado uma lista com as notas dos alunos de uma turma, retorna uma lista com os aprovados
    list->list'''
    x=lista
    y=sum(x)
    x.append(y)
    list.sort(x)
    z=x.index(y)
    w=len(x)
    return lista[z+1:w]