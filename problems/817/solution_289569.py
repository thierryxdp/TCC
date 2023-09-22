def acima_da_media (lista):
    ''' função que dada uma lista com as notas dos alunos de uma turma
        retorne uma lista ordenada com as notas que ficarem a cima da
        média entre eles
        [list-->list]'''
    T = sum(lista)
    M = T/(len(lista))
    lista = lista + [M]
    list.sort(lista)
    p1 = list.count(lista,M)
    p2 = list.index(M)
    A = lista[p1+p2:]
     return A