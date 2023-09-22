def acima_da_media(n):
    media = sum(n)/len(n)
    list.append(n, media)
    a = list.index(n, media)
    b = n[media+1:]
    return b