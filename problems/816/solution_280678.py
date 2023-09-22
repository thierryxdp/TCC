def maiores(l,n):
    if n in l:
        l.sort()
        i = list.index(l,n)
        return l[i+1:]
    else:
        l.append(n)
        l.sort()
        i = list.index(l,n)
        return l[i+1:]