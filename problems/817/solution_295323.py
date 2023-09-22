def acima_da_media(lista):
    newlist = lista
    quant_nota = len(newlist)
    media = int(sum(newlist)/quant_nota)
    list.sort(newlist)
    list.append(newlist, media)
    list.count(newlist, media)
    return newlist