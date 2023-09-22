def acima_da_media(lista,nota):
    """..."""
    if nota not in lista:
        list.append(lista,nota)
    list.sort(lista,nota)
    indice = list.index(lista,nota)
    lista_media = lista[indice+1:]
    return lista_media