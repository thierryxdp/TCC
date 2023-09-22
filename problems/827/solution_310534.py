def qtd_divisores(n):
    x=[]
    i=1
    while i in range(1,n+1):
        if n%i==0:
            x.append(i)
        i+=1
    return len(x)