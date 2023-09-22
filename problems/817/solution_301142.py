def acima_da_media (lista_notas):
    '''retorna uma nova lista ordenada com as notas da lista_notas que ficaram acima da média
    list -> list'''
    lista_acima_media = []
    media = lista_notas.sum() / len(lista_notas)
    contador = 0
    while contador < len(lista_notas):
        if lista_notas[contador] > media:
            lista_acima_media.append(lista_notas[media])
    	contador += 1
    lista_acima_media.sort()
    return lista_acima_media