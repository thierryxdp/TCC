def qtd_divisores(n):
    x=1
    l=[]
    while x <= n:
        if n%x==0:
            
            l.append(x)
        else l=l
        x+=1
    return len(l)