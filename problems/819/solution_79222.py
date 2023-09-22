def filtraMultiplos(l,n):
    i=0
    divisiveis=[]
    while i<len(l):
        if l[i]%n==0:
            divisiveis=divisiveis+[l[i]]
        i=i+1
    return divisiveis