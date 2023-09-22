def acima_da_media(l):
    media = sum(l)/len(l)
    l.append(media)
    l.sort(reverse=True)
    i = l.index(media)
    l = l[:i]
    l.sort()
    return l