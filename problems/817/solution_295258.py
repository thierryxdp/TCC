def acima_da_media(lista):
    """ Dada uma lista com as notas dos alunos de uma turma, retorna uma segunda lista com as notas que ficaram acima da média;
    list->list """
    lista2=[x for x in lista if x>=7]
    list.sort(lista2)
    return lista2