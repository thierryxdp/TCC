def fatorial(num):
    i=0
    l=list(range(num,0,-1))
    while i<len(l):
        l[i]=l[i]*l[i+1]
        i=i+1
    return l