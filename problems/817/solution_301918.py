def ordena(l):
    list.sort(l)
    return l
def acima_da_media(l):
    l = ordena(l)
    r = int(sum(l)/len(l))
    for n in l:

        l = l[list.index(l, n>r):]
    return l