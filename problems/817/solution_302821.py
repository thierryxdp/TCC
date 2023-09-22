def acima_da_media(lista):

    """Dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da média

    list -> list"""

    x = lista

    a = sum(x)

    b = len(x)

    c = a/b

    list.insert(x, -1, c)

    a = sorted(x)

    b = list.index(a, c)

    del a[:b + list.count(a,c):1]

    return a