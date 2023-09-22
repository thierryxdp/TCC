from math import ceil
def acima_da_media(lista):
    '''funcao que dado uma lista com as notas dos alunos de uma turma, retorna uma lista com os aprovados
    list->list'''
    x=lista
    y=ceil((sum(x))/len(x))
    t=x.count(y)
    x.append(y)
    list.sort(x)
    w=x.index(y)
    z=len(x)
    if count==1:
        return x[w+1:z]
    elif count>1:
        return x[w+2:z]