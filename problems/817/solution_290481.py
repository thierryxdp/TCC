from math import ceil
def acima_da_media(lista):
    '''funcao que dado uma lista com as notas dos alunos de uma turma, retorna uma lista com os aprovados
    list->list'''
    x=lista
    y=ceil((sum(x))/len(x))
    z=len(x)
    if y in x:
        return x[y+1:z]
    elif y not in x:
        x.append(y)
        list.sort(x) 
        w=x.index(y)
        z=len(x)
        return x[w+1:z]