def acima_da_media(notas: list[float]):
    media = sum(notas)/len(notas) 
    notas.append(media)
    notas.sort()
    k = notas[-1]
    l = notas[-2]
    m = notas[-3]
    n = notas[-4]
    o = notas[-5]
    p = notas[-6]
    q = notas[-7]
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