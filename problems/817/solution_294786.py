def acima_da_media(lista):
    """Dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com
    as notas que ficaram acima da média,list->list"""
    list.sort(lista)
    x=list.index(lista,6)
    return lista[x:]