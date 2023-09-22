import math
def acima_da_media(lista:list)->list:
    """Função que, dado uma lista, retorna a media das notas do aluno, junto a lista ordenada das notas acima da media.
    """
    media_notas = sum(lista)/len(lista)
    list.append(lista,media_notas)
    list.sort(lista)
    posicao=list.index(lista,media_notas)+1
    if media_notas==float(lista[(list.index(lista,media_notas)])+1
        return (lista[posicao:])
    else:
        return (lista[posicao+1:])