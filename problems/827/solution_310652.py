def qtd_divisores(n):
    r=[]
    i=1
    while i<=n:
        if n%i==0:
            r.append(i)
        i=i+1
    return len(r)