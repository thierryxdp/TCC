def faltante(l):
    i=0
    for x in l:
        if x-l[i-1]!=1 and i>0:
            return x-1
        i=i+1
    return i+1