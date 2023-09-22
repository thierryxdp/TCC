def acima_da_media(lista_notas,media):
    list.append(lista_notas,media)
    list.sort(lista_notas)
    po = list.index(lista_notas,media)
    del lista_notas[0:po]
    return lista_notas