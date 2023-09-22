def acima_da_media(lista):
    newlist = lista
    quant_nota = len(newlist)
    media = int(sum(newlist)/quant_nota)
    list.append(newlist, media)
    list.count(newlist, media)
    list.sort(newlist)
    a = list.index(newlist,media)
    return a