def acima_da_media(lista_nota):
    media = sum(lista_nota)/len(lista_nota)
    if media in lista_nota:
        list.sort(lista_nota)
        lista = lista_nota[list.index(lista_nota,media)+1:]
        return lista
    else:
        list.append(lista_nota,media)
        list.sort(lista_nota)
        lista = lista_nota[list.index(lista_nota,media)+1:]
        return lista