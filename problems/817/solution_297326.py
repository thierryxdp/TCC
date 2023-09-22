def acima_da_media(lista):
    """Função que dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da média."""
    M = (sum(lista))/(len(lista))
    list.append(lista,M)
    list.sort(lista)
    return lista[((list.index(lista,M)))+1:]