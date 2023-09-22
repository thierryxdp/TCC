def acima_da_media(lista):
    '''Dada uma lista com a nota dos alunos, essa função retorna uma lista ordenada
    com as notas que ficaram acima da media da turma
    list-->list'''
    lista1=lista[:]
    media=sum(lista1)/len(lista1)
    list.append(lista1,media)
    list.sort(lista1)
    lista1=lista1[list.index(lista1,media)+1:]
    return lista1