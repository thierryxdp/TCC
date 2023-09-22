def acima_da_media(lista_de_notas,media):
    return sorted(lista_de_notas)[(list.index(sorted(lista_de_notas + [media]),media))