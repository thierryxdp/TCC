def faltante(l):
    i=0
    a=list(range(len(l)+2))[1:]
    if l not in a:
        return sum(a)-sum(l)
    else:
        while i<len(a):
            if l[i]!=a[i]:
                x=a[i]
            else:
                i=i+1
    return x