def ordena(l):
    list.sort(l)
    return l
def acima_da_media(l):
    
    if 5 in l:
        l = l[list.index(l, 5):]
	elif 6 in l:
        l = l[list.index(l, 6):]
    elif 7 in l:
        l = l[list.index(l, 7):]
    elif 8 in l:
        l = l[list.index(l, 8):]
    elif 9 in l:
        l = l[list.index(l, 9):]
    elif 10 in l:
        l = l[list.index(l, 10):]
    return l