def repetidos(l):
    x=0
    i=0
    for e in l:
        if e==(l[i-l]):
            i= i+1
        else:
            x= x
            i =i+1
    return x