def acima_da_media(lista):
    """funcao que dada uma lista com as notas dos alunos, retorna uma lista ordenada com as
    notas que ficaram acima da media;
    list -> list"""
    list.sort(lista)
    media = int(sum(lista)/len(lista))
    if max(lista) == media:
        return []
    if media == 0:
        return[]
    else:
        del lista[0:media+1]
        return lista