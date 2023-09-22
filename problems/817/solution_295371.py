import math
def acima_da_media(notas):
    newlist = notas
    media = int(sum(newlist)/len(notas))
    list.append(newlist, media+1)
    list.sort(newlist)
    nposition = list.index(newlist, media)
    return newlist[nposition:]