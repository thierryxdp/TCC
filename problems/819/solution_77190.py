def filtramultiplos(v,n):
    x=0
    v=[]
    while x<len(v):
        if n//x==0:
            x=x+1
            list.append(v,x)
    return v