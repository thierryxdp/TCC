def acima_da_media(lista):
    '''funcao que dado uma lista com as notas dos alunos de uma turma, retorna uma lista com os aprovados
    list->list'''
    x=lista
    x.append(7)
    list.sort(x)
    y=x.index(7)
    w=len(x)
    return lista[y+1:w]