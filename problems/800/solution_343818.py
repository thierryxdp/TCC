def total (ls,d):
    return map(ls, lambda s: d[s])
def lc (ls,d):
    return reduce(total(ls,d), lambda x,y: x + y,0)