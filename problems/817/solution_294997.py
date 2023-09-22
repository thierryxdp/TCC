def acima_da_media(lista):
    """Função que dada uma lista com as notas dos alunos
       retorna uma lista ordenada com as notas que ficaram
       acima da média.
       list->list"""
    media = sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    if media == list.index(lista,media,0):
        return list.del(lista,media)
    else:
        return lista[lista.index(media)+1:]