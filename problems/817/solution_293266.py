def acima_da_media(lista):
    """função que dada a lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média;list->list"""
    media=sum(lista)/len(lista)
    lista.append(media)
    lista.sort()
    return lista[:]