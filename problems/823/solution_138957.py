def faltante(x):
    if x[0]!=1:
        return 1
    elif len(x)==x[len(x)-1]:
        return len(x)+1
    for i in x:
        if x[i]!=i+1:
            return x[i]+1