def acima_da_media(lista):
    """
    Dada uma lista de notas de um aluno calcula a sua média e retorna as notas que estão
    acima da média.
    :param lista_notas: list -> list
    :return: list -> list
    """
    media = ceil(sum(lista_notas) / len(lista_notas))
    lista_notas.append(media)
    organizaLista = sorted(lista_notas)
    indiceMedia = organizaLista.index(media)
    media = int(sum(lista) / len(lista))
    lista.append(media)
    listaOrganizada = sorted(lista)
    indiceMedia = listaOrganizada.index(media)
    novaLista = listaOrganizada[indiceMedia + 1:].copy()

    if media not in organizaLista:
        lista_notas.append(media)
    if media in novaLista:
        del novaLista[0]

    return organizaLista[indiceMedia + 1:] 
    return novaLista