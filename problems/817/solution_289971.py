def acima_da_media(notas):
    '''dada uma lista de entrada com as notas dos alunos, retorna uma lista ordenada com as notas que ficaram acima da média
    list->list'''
    m = sum(notas)/ len(notas)
    lista = notas + [m]
    list.sort(lista)
    x = list.index(lista,m)
    y = list.count(lista,m)
    return lista[x + y:]