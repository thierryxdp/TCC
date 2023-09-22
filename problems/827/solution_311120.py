def qtd_divisores(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            list.append(l,i)
    return len(l)