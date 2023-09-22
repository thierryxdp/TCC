def acima_da_media(l):
    media = sum(l)/len(l)
    l.append(media)
    l.sort()
    i = l.index(media)
    return l[i+1:]