def faltante(l):
    l[-1]=0
    f=0
    i=0
    for x in l:
        if x-l[i-1]!=1:
           	faltante=x-1
        i=i+1
    return i+1