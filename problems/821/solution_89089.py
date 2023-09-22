def fatorial(num):
    i=0
    l=list(range(num-1,0,-1))
    g=[]
    while i<num:
        if i==1:
            g=i*num
        if i>1:
            g=g[0]*i
        i=i+1
    return g