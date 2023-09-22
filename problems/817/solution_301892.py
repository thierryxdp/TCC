def ordena(l):
    list.sort(l)
    return l
def acima_da_media(l):
    l = ordena(l)
    if 5 in l:
    	l = l[list.index(l, 5):]
        elif 6 in l:
            l = l[list.index(l, 6):]
    return l