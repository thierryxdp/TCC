def acima_da_media(lista):
    """Retorna uma lista ordenada com as notas que ficaram acima da media dados:
    uma lista com as notas dos alunos"""

    media=int(sum(lista)/len(lista))
    lista.append(media)
    listaO=sorted(lista)
    indiceM=listaO.index(media)
    listaN=listaO[indiceM+1:].copy()

    if media in listaN:
        del listaN[0]

    return listaN