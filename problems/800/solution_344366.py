def mapeia(ls,y):
    l=[]
    for e in ls:
        l.append(y(e))
    return l


def total(ls,d):
    return round(sum(mapeia(ls,lambda x:d[x])),2)