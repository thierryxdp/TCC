def acima_da_media(lista):
    '''Recebe uma lista com as notas dos alunos de uma turma e retorna uma 
    lista ordenada com todas as notas que ficaram acima da media;
    list -> list'''
    x=sum(lista)
    y=int(x/len(lista))
    list.append(lista,y)
    list.sort(lista)
    z=list.index(lista,y)
    return lista[z+1:]