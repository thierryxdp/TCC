def acima_da_media(lista):
    """Função que dada uma lista com as notas dos alunos
       retorna uma lista ordenada com as notas que ficaram
       acima da média.
       list->list"""
    media = sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    return lista[lista.index(media)+0.001:]