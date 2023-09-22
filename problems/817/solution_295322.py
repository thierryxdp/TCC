def acima_da_media(lista):
    newlist = lista
    quant_nota = len(newlist)
    media = sum(newlist)/quant_nota
    list.sort(newlist)
    return newlist