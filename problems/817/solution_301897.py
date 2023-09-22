def ordena(l):
    list.sort(l)
    return l
def acima_da_media(l):
    l = ordena(l)
    for media in l:
        l = l[list.index(l, media):]
        media < = 5
    return l