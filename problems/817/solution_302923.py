from math import*
def acima_da_media(lista):
    """ Dada uma lista com notas dos alunos de uma turma, 
    retorna uma lista ordenada com as notas que ficaram acima da média.
    :param lista_notas: list -> list
    :return: list -> list
    """
    media = int(sum(lista) / len(lista))
    lista.append(media)
    lista01 = sorted(lista)
    indiceMedia = lista01.index(media)
    novaLista = lista01[indiceMedia + 1:].copy()

    if media in novaLista:
        del novaLista[0]

    return novaLista