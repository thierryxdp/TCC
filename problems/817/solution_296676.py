def acima_da_media(notas: list[float]):
    media = sum(notas)/len(notas) 
    notas.append(media)
    notas.sort()
    k = notas[-1] or 0
    l = notas[-2] or 0
    m = notas[-3] or 0
    n = notas[-4] or 0
    o = notas[-5] or 0
    p = notas[-6] or 0
    q = notas[-7] or 0
    if q == media:
        return [p,o,n,m,l,k]
    elif p == media:
        return [o,n,m,l,k]
    elif o == media:
        return [n,m,l,k]
    elif n == media:
        return [m,l,k]
    elif m == media:
        return [l,k]
    elif l == media:
        return [k]
    else:
        return []