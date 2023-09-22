def faltante(l):
    ''
    list.sort(l)
    prox=0
    pp=1
    while prox<len(l) and pp<len(l):
        if l[prox]-l[pp]==-2:
            return l[prox]+1
        prox=prox+1
        pp=pp+1
        else:
            return l[prox]+1