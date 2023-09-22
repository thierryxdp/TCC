def acima_da_media(lista: list) -> list:
    """ dado uma lista, pega a nota de um grupo de alunos e retorna
    uma lista ordenada com as notas dos que ficaram acima da média """

    list.sort(lista)

    a = sum(lista)/len(lista)

    list.append(lista, a)

    list.sort(lista)
    del lista[:list.index(lista, a) + list.count(lista, a)]

    return lista