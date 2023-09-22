def media(v):
    return sum(v)/len(v)
def maiores (J, n):
    list.append(J, n)
    list.sort(J)
    e = list.index(J, n)
    del J[:(e+1)]
    return J
def acima_da_media(j):
    return maiores(j, media(j))