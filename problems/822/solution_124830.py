def repetidos(l):
    x=0
    i=1
    while i<len(l):
        if l[i]==l[i-1]:
            x=x+1
        i=i+1
    return x