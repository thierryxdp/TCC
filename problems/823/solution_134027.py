def faltante(l):
    l.sort()
    x=0
    while x<len(l):
        if l[x]!=x+1:
            return x+1