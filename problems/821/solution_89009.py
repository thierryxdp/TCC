def fatorial(num):
    i=0
    l=list(range(num,0,-1))
    l1=[]
    while i<=num:
        l1=num*l[i]
        i=i+1
    return l1