def acima_da_media(notas):
    newlist = notas
    media = (int(sum(newlist)/len(notas)))
    list.append(newlist, media)
    list.sort(newlist)
    nposition = list.index(newlist, media)
    if nposition == len(newlist)-1:
        return newlist[nposition]
    else:
    	return newlist[nposition:]