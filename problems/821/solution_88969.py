def fatorial(num):
    i=1    
    l=list(range(num,0,-1))
    l1=[num,]
    while i<=num:
        l1=l1*l[i]                  
    return l1