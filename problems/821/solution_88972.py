def fatorial(num):
    i=1    
    l=list(range(num+1,0,-1))
    l1=[num]
    while i<=num:
        l1=list.pop(l1[0])*l[i]
        i=i+1
    return l1