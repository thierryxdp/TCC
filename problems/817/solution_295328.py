def acima_da_media(lista):
    newlist = lista
    quant_nota = len(newlist)
    media = int(sum(newlist)/quant_nota)
    list.append(newlist, media)
    list.sort(newlist)
    var1 = list.count(newlist, media)
    if var1 == 1:
        var2 = list.index(newlist, media)
        return newlist[var2:]
    else:
        return newlist