def faltante(l):
    l=l.sort()
    x=1
    while x<len(l):
        if l[x]!=x:
            return x