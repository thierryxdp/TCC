def qtd_divisores(n):
    x=1
    l=[]
    while x <= n:
        n%x==0:
            
            l+=x
        x+=1
    return len(l)