def fatorial(num):
    i=0
    ii=1
    l=list(range(num,0,-1))
    l1=[]
    while i<num:
        l1=l[i]*l[i+ii]
        i=i+1
    return l1