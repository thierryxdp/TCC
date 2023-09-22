from math import floor
def acima_da_media(lista):
    """
    Dada uma lista de notas de um aluno calcula a sua média e retorna as notas que estão
    acima da média.
    :param lista_notas: list -> list
    :return: list -> list
    """
    media = int(sum(lista) / len(lista))
    lista.append(media)
    listaOrganizada = sorted(lista)
    indiceMedia = listaOrganizada.index(media)
    novaLista = listaOrganizada[indiceMedia + 1:].copy()
    if media in novaLista:
        
        del novaLista[0]
        
        return novaLista