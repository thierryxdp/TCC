def filtraMultiplos(l,n):
    r=[]
    proximo=0
    while proximo<len(l):
        if l[proximo]%n==0:
            list.append(r,l[proximo]) # = r.append(l[proximo])
        proximo=proximo+1
    return r