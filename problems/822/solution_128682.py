def repetidos(x):
    l1=x[1:]
    i=0
    d=[]
    while i<len(x):
        if x[i]==l1[i]:
            return d.append(i)
        i+=1
    return len(d)