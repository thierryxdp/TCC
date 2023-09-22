def acima_da_media(lista):
    media = round(int(sum(lista))/int(len(lista)),0)
    list.append(lista,media)
    list.sort(lista)
    return lista[list.index(lista,media)+1:]