def fatorial(n):
    i=0
    a=list(range(n))[1:]+[n]
    b=-1
    
    while i<len(a):
            fatorial_num=a[i]*a[i+1]
            i=i+1
    return fatorial_num