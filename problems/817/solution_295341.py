import math
def acima_da_media(notas):
    newlist = notas
    media = math.floor(int(sum(newlist)/len(notas)))
    list.append(newlist, media)
    list.sort(newlist)
    n_position = list.index(newlist, media+1)
    return newlist[n_position:]