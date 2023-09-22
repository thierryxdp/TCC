def acima_da_media(lista):
    media = (sum(lista))/len(lista)
    if media not in lista:
        list.append (lista,(media))
        list.sort(lista)
        rank = list.index(lista, media)
        resp= lista[rank+1:]
        return resp
    if media in lista:
        list.sort(lista)
        rank = list.index(lista, media)
        resp2= lista[rank+1:]
        return resp2