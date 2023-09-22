def precos(ls,d):
    return map(ls, lamda s: d[s])
def lc(ls,d):
    return sum(precos(ls,d))