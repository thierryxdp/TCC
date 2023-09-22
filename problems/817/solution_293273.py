def acima_da_media(lista):
    """função que dada a lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média;list->list"""
    media=sum(lista)/len(lista)
    lista.append(media)
    lista.sort()
    index= lista.index(media)
    if (media==lista[index]+2):
        return lista[index+2:]
    else:
        return lista[index+1:]