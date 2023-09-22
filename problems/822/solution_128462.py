def repetidos(x):
    n=[]
    c=0
    while c<len(x):
        if x[c]==x[c+1]:
            n+=1
    return n