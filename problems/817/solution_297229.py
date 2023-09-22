from math import floor

def acima_da_media(lista):
    """
    Dada uma lista de notas de um aluno calcula a sua média e retorna as notas que estão
    acima da média.
    list -> list
    """
    media = int(sum(lista) / len(lista))
    lista.append(media)
    lista_Organizada = sorted(lista)
    indicem = lista_Organizada.index(media)
    novaLista = lista_Organizada[indicem + 1:].copy()

    if media in novaLista:
        del novaLista[0]

    return novaLista