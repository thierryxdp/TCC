import math
def acima_da_media(lista_notas):
    """A funcao recebe uma lista de notas e retorna uma lista apenas com notas acima da media.
    list ->list"""
    media=int(math.floor(sum(lista_notas)/len(lista_notas)))
    if media in lista_notas:
        list.append(lista_notas,media)
        list.sort(lista_notas)
        ocorrencia=list.index(lista_notas,media)
        return lista_notas[ocorrencia+2:]
    else:
        list.append(lista_notas,media)
        list.sort(lista_notas)
        ocorrencia=list.index(lista_notas,media)
        return lista_notas[ocorrencia+1:]