import math
def acima_da_media(lista):
    '''Função que retorna as notas dos alunos que ficaram acima da média;
    list -> list'''
    l=(sum(lista)/len(lista))
    list.append(lista,l)
    list.sort(lista)
    i=list.index(lista,l)
    n=lista[i]
    del lista[:i+1]
    if n in lista:
        list.remove(lista,n)
        return lista
    else:
        return lista