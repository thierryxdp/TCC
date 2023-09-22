def acima_da_media(lista):
    media=sum(lista)/len(lista)
    y=list.append(lista,media)
    x=list.sort(lista)
    if media in lista:
        return lista[list.index(lista,media)+1:]