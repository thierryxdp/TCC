def acima_da_media(lista):
    """ dada uma lista com as notas dos alunas de uma turma, retorna uma lista
    ordenada com as notas que ficaram acima da média.
    list -> list """
    a = len(lista)
    b = sum(lista)
    c = b/a
    list.sort(c)
    return c