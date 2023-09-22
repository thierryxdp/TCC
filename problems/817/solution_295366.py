import math
def acima_da_media(notas):
    newlist = notas
    media = sum(newlist)/len(notas)
    list.append(newlist, math.ceil(media))
    list.sort(newlist)
    nposition = list.index(newlist, media+1)
    return newlist[nposition:]