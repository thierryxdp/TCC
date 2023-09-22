def acima_da_media(lista):
    '''Define as notas que ficaram acima da média
    list -> list'''
    elementos = len(lista)
    soma = sum(lista)
    media = soma/elementos
    lista.append(media)
    list.sort(lista)
    indice = list.index(lista, media)
    contagem = list.count(lista, media)
    return lista[indice+contagem: ]