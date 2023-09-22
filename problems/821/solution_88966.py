def fatorial(num):
    i=0
    I=1
    l=list(range(num,0,-1))
    l1=[]
    while i<=num:
        l1=l[i]*l[i+I]
        i=i+1
    return l1