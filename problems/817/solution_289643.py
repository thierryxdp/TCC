def acima_da_media(notas):
    a=notas
    media= sum(a)/len(a)
    list.append(a, media)
    a.sort()
    posmedia= list.index(a, media)
    return a[posmedia+1:]