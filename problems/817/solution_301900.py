def ordena(l):
    list.sort(l)
    return l
def acima_da_media(l):
    l = ordena(l)
    l = l[str.find(l, 5):]
    return l