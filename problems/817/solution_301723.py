def maiores (l, n):
    list.append (l, n)
    list.sort (l)
    return l[((list.index(l,n)) + 1): ]
def acima_da_media (l):
    if sum (l) > 6:
        return maiores
    else:
        return ()