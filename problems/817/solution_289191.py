def acima_da_media(lista_de_notas,média):
    return sorted(lista_de_notas)[(list.index(sorted(lista_de_notas + [média]),média))