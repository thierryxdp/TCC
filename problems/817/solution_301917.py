def ordena(l):
    list.sort(l)
    return l
def acima_da_media(l):
    l = ordena(l)
    r = int(sum(l)/len(l))
    l = l[list.index(l, r+1):]
    return l