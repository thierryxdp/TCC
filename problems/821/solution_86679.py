def fatorial(n):
    i=0
    a=list(range(n))[1:]+[n]
    fatorial_num=1
    
    
    while i<len(a):
            fatorial_num=fatorial_num*i
            i=i+1
    return fatorial_num