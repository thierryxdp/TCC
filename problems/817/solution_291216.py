def acima_da_media(lista):
    """
    Dada uma lista de notas de um aluno calcula a sua média e retorna as notas que estão
    acima da média.
    :param lista_notas: list -> list
    :return: list -> list
    """
    list(lista)
    media = int(sum(lista) / len(lista))
    lista.append(media)
    listaOrganizada = sorted(lista)
    indiceMedia = listaOrganizada.index(media)

    if media not in listaOrganizada:
        lista.append(media)

    return listaOrganizada[indiceMedia + 1:]