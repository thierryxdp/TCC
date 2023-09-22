from math import floor

def acima_da_media(lista_notas):
    """
    Dada uma lista de notas de um aluno calcula a sua média e retorna as notas que estão
    acima da média.
    :param lista_notas: list -> list
    :return: list -> list
    """
    media = floor(sum(lista_notas) / len(lista_notas))
    lista_notas.append(media)
    organizaLista = sorted(lista_notas)
    indiceMedia = organizaLista.index(media)

    if media in organizaLista:
        del organizaLista[indiceMedia]

    return organizaLista[indiceMedia + 1:]