def fatorial(num):
    i=0
    l=list(range(num,0,-1))
    l1=[]
    while i<num:
        l1=l[i]*l[i+1]
        i=i+1
    return l1