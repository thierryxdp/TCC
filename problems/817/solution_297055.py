def acima_da_media (lista_notas):
    import math
    media = math.ceil((sum(lista_notas))/(len(lista_notas)))
    lista_notas.append(media)
    list.sort(lista_notas)
    centro = lista_notas.index(media)
    lista2 = lista_notas[centro:]
    lista2.remove(media)
    return lista2