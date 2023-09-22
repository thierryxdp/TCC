def acima_da_media(notas):
    newlist = notas
    media = (int(sum(newlist)/len(notas)))
    list.append(newlist, media)
    list.sort(newlist)
    n_position = list.index(newlist, media)
    return newlist[n_position:]