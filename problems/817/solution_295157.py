def acima_da_media(n):
    media = sum(n)/len(n)
    list.append(n, media)
    list.sort(n)
    a = list.index(n, media)
    b = n[a+1:]
    if b[0] == media:
        c = b[1:]
        return c
    if b[0] != media:
        return b