def acima_da_media(lista):
    '''retorna uma lista ordenada com as notas que ficaram acima da media geral da lista
    list -> list'''
    media = (sum(lista))/len(lista)
    list.append(lista,media)
    list.sort(lista)
    posicao = list.index(lista,media)
    return lista[posicao+1:]