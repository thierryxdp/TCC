def precos(ls,d):
    return map(ls, lambda s:d[s])

def lc(ls,d):
    return sum(precos(ls,d))