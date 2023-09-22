def faltante(x):
    l1=x[1:]
    i=0
    if x[0]!= 1:
        return 1
    if x[len(x)-1]==len(x):
        return len(x)+1
    while i < len(x):
        if x[i]!=l1[i]-1:
            return l1[i]-1
    i+=1