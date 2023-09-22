def mapeia(f, d, ls):
    ret = []
    for e in ls:
        list.append(ret, f(d, e))
    return tuple(ret)

def total(ls, d):
    return round(sum(mapeia(lambda d, e: d[e], d, ls)), 2)