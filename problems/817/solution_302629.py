def acima_da_media(lista):
    """funcao que dada uma lista com as notas dos alunos, retorna uma lista ordenada com as
    notas que ficaram acima da media;
    list -> list"""
    media = int(sum(lista)/len(lista))
    if media not in lista:
    	list.insert(lista, 1, media)
    	list.sort(lista)
        x = list.index(lista, media)
        del lista[0:x+1]
        return lista
    if media == 0:
        return[]
    else:
        x = list.index(lista, media)
        del lista[0:x+1]
        return lista